import threading
import time
import typing
from ..authtoken.auth.raw_client import RawAuthClient
from ..core.client_wrapper import SyncClientWrapper
import httpx

class OAuthTokenProvider:
    """Simple OAuth token provider with caching."""
    
    BUFFER_SECONDS = 120  # 2 minutes
    TOKEN_LIFETIME = 3600  # 1 hour

    def __init__(self, username: str, password: str, base_url: str):
        self._username = username
        self._password = password
        self._base_url = base_url
        self._lock = threading.Lock()
        self._access_token: typing.Optional[str] = None
        self._expires_at: float = 0.0

    def __call__(self) -> str:
        """Get a valid token, refreshing if necessary."""
        with self._lock:
            if self._is_token_expired():
                self._get_fresh_token()
            assert self._access_token is not None
            return self._access_token

    def _is_token_expired(self) -> bool:
        """Check if current token is expired or about to expire."""
        now = time.time()
        return self._access_token is None or now > self._expires_at - self.BUFFER_SECONDS

    def _get_fresh_token(self):
        """Get a fresh token using the raw auth client."""
        # Create a simple client wrapper that doesn't try to get tokens
        httpx_client = httpx.Client(timeout=60)
        client_wrapper = SyncClientWrapper(
            base_url=self._base_url,
            token="",  # No token needed for auth requests
            headers={},
            httpx_client=httpx_client,
            timeout=60
        )
        
        # Use the raw auth client
        raw_auth_client = RawAuthClient(client_wrapper=client_wrapper)
        token_response = raw_auth_client.generate_token(
            username=self._username,
            password=self._password
        )
        
        self._access_token = token_response.data.token
        self._expires_at = time.time() + self.TOKEN_LIFETIME

def create_token_provider(username: str, password: str, base_url: str) -> typing.Callable[[], str]:
    """Create token provider."""
    return OAuthTokenProvider(username, password, base_url) 