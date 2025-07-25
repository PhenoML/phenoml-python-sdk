import threading
import time
import typing
import base64
from ..authtoken.client import AuthtokenClient, AsyncAuthtokenClient
from ..core.request_options import RequestOptions

class OAuthTokenProvider:
    """
    Provides a cached OAuth token, refreshing it using username/password if expired or about to expire.
    Sync version for use with phenoml client.
    """
    BUFFER_SECONDS = 120  # 2 minutes

    def __init__(
        self,
        *,
        username: str,
        password: str,
        authtoken_client: AuthtokenClient,
    ):
        self._username = username
        self._password = password
        self._authtoken_client = authtoken_client
        self._lock = threading.Lock()
        self._access_token: typing.Optional[str] = None
        self._expires_at: float = 0.0

    def __call__(self) -> str:
        with self._lock:
            now = time.time()
            if self._access_token is None or now > self._expires_at - self.BUFFER_SECONDS:
                basic_auth = base64.b64encode(f"{self._username}:{self._password}".encode()).decode()
                token_response = self._authtoken_client.generate_token(
                    request_options=RequestOptions(
                        additional_headers={
                            "Authorization": f"Basic {basic_auth}"
                        }
                    )
                )
                self._access_token = token_response.token
                # Assume token is valid for 1 hour if no expiry info is provided
                self._expires_at = now + 3600
            return self._access_token

class AsyncOAuthTokenProvider:
    """
    Provides a cached OAuth token, refreshing it using username/password if expired or about to expire.
    Async version for use with Asyncphenoml client.
    """
    BUFFER_SECONDS = 120  # 2 minutes

    def __init__(
        self,
        *,
        username: str,
        password: str,
        authtoken_client: AsyncAuthtokenClient,
    ):
        self._username = username
        self._password = password
        self._authtoken_client = authtoken_client
        self._lock = threading.Lock()
        self._access_token: typing.Optional[str] = None
        self._expires_at: float = 0.0

    async def __call__(self) -> str:
        # Use a thread lock to avoid race conditions in async context
        with self._lock:
            now = time.time()
            if self._access_token is None or now > self._expires_at - self.BUFFER_SECONDS:
                basic_auth = base64.b64encode(f"{self._username}:{self._password}".encode()).decode()
                token_response = await self._authtoken_client.generate_token(
                    request_options=RequestOptions(
                        additional_headers={
                            "Authorization": f"Basic {basic_auth}"
                        }
                    )
                )
                self._access_token = token_response.token
                self._expires_at = now + 3600
            return self._access_token 