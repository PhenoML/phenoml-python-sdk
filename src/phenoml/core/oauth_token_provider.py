import threading
import time
import typing
import base64
import asyncio
from ..authtoken.client import AuthtokenClient, AsyncAuthtokenClient
from ..core.request_options import RequestOptions

class BaseOAuthProvider:
    """Base class for OAuth token providers with common caching logic."""
    
    BUFFER_SECONDS = 120  # 2 minutes
    TOKEN_LIFETIME = 3600  # 1 hour

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        self._lock = threading.Lock()
        self._access_token: typing.Optional[str] = None
        self._expires_at: float = 0.0

    def _is_token_expired(self) -> bool:
        """Check if current token is expired or about to expire."""
        now = time.time()
        return self._access_token is None or now > self._expires_at - self.BUFFER_SECONDS

    def _create_basic_auth_header(self) -> str:
        """Create Basic Auth header from username/password."""
        credentials = f"{self._username}:{self._password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded}"

    def _update_token_cache(self, token: str):
        """Update the cached token and expiry time."""
        self._access_token = token
        self._expires_at = time.time() + self.TOKEN_LIFETIME


class OAuthTokenProvider(BaseOAuthProvider):
    """Synchronous OAuth token provider for sync clients."""

    def __init__(self, username: str, password: str, authtoken_client: AuthtokenClient):
        super().__init__(username, password)
        self._authtoken_client = authtoken_client

    def __call__(self) -> str:
        """Get a valid token, refreshing if necessary."""
        with self._lock:
            if self._is_token_expired():
                token_response = self._authtoken_client.generate_token(
                    request_options=RequestOptions(
                        additional_headers={"Authorization": self._create_basic_auth_header()}
                    )
                )
                self._update_token_cache(token_response.token)
            assert self._access_token is not None  # Type guard
            return self._access_token


class AsyncOAuthTokenProvider(BaseOAuthProvider):
    """Asynchronous OAuth token provider for async clients."""

    def __init__(self, username: str, password: str, authtoken_client: AsyncAuthtokenClient):
        super().__init__(username, password)
        self._authtoken_client = authtoken_client

    def __call__(self) -> str:
        """Synchronous access to token. Creates new event loop if needed."""
        try:
            # Try to get running loop
            asyncio.get_running_loop()
            raise RuntimeError("Cannot call async provider from async context. Use get_token_async()")
        except RuntimeError:
            # No running loop, create one
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                token = loop.run_until_complete(self._get_fresh_token())
                assert token is not None  # Type guard
                return token
            finally:
                loop.close()

    async def get_token_async(self) -> str:
        """Async access to token."""
        with self._lock:
            if self._is_token_expired():
                await self._get_fresh_token()
            assert self._access_token is not None  # Type guard
            return self._access_token

    async def _get_fresh_token(self) -> str:
        """Fetch a fresh token from the server."""
        token_response = await self._authtoken_client.generate_token(
            request_options=RequestOptions(
                additional_headers={"Authorization": self._create_basic_auth_header()}
            )
        )
        self._update_token_cache(token_response.token)
        assert self._access_token is not None  # Type guard
        return self._access_token


def create_token_provider(username: str, password: str, authtoken_client) -> typing.Callable[[], str]:
    """Create appropriate token provider based on client type."""
    if isinstance(authtoken_client, AsyncAuthtokenClient):
        provider: typing.Union[OAuthTokenProvider, AsyncOAuthTokenProvider] = AsyncOAuthTokenProvider(username, password, authtoken_client)
    else:
        provider = OAuthTokenProvider(username, password, authtoken_client)
    
    return provider 