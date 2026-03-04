"""
Simple wrapper that extends the base client with automatic token generation.
"""

import httpx
from typing import Optional, Union, Callable

from .client import phenoml, Asyncphenoml
from .environment import phenomlEnvironment
from .authtoken.client import AuthtokenClient, AsyncAuthtokenClient
from .core.client_wrapper import SyncClientWrapper, AsyncClientWrapper


class PhenoMLClient(phenoml):
    """
    Extends the base client with automatic token generation from username/password.
    """
    
    def __init__(
        self,
        *,
        token: Optional[Union[str, Callable[[], str]]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        **kwargs
    ):
        # Validate authentication
        if token is None and (username is None or password is None):
            raise ValueError("Must provide either 'token' or both 'username' and 'password'")
        
        if token is not None and (username is not None or password is not None):
            raise ValueError("Cannot provide both 'token' and 'username'/'password'")
        
        # Generate token if needed
        if token is None:
            if username is None or password is None:
                raise ValueError("Must provide both 'username' and 'password'")
            base_url = kwargs.get('base_url')
            if base_url is None:
                raise ValueError("Must provide 'base_url' when using username/password")
            token = self._generate_token(username, password, base_url)
        
        # Wrap string token in a callable
        if isinstance(token, str):
            _token_str = token
            token_getter: Callable[[], str] = lambda: _token_str
        else:
            token_getter = token
        
        # The parent constructor requires client_id and client_secret, but when
        # using _token_getter_override, the OAuth flow is bypassed. We pass
        # placeholder values to satisfy the parent's validation.
        super().__init__(
            client_id=client_id or "wrapper-managed",
            client_secret=client_secret or "wrapper-managed",
            _token_getter_override=token_getter,
            **kwargs
        )
    
    def _generate_token(self, username: str, password: str, base_url: str) -> str:
        """Generate token using the auth client."""
        # Create a simple client wrapper without authentication
        client_wrapper = SyncClientWrapper(
            base_url=base_url,
            httpx_client=httpx.Client()
        )
        
        # Create the auth client using the existing SDK
        auth_client = AuthtokenClient(client_wrapper=client_wrapper)
        
        response = auth_client.auth.generate_token(username=username, password=password)
        return response.token


class AsyncPhenoMLClient(Asyncphenoml):
    """
    Extends the async base client with automatic token generation from username/password.
    """
    
    def __init__(
        self,
        *,
        token: Optional[Union[str, Callable[[], str]]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        **kwargs
    ):
        # Validate authentication
        if token is None and (username is None or password is None):
            raise ValueError("Must provide either 'token' or both 'username' and 'password'")
        
        if token is not None and (username is not None or password is not None):
            raise ValueError("Cannot provide both 'token' and 'username'/'password'")
        
        # Store for async token generation (needed for initialize)
        self._username = username
        self._password = password
        self._base_url = kwargs.get('base_url')
        if token is None and self._base_url is None:
            raise ValueError("Must provide 'base_url' when using username/password")
        
        # Create with temporary token if needed
        self._current_token = ""
        
        if token is not None:
            if isinstance(token, str):
                _token_str = token
                token_getter: Callable[[], str] = lambda: _token_str
            else:
                token_getter = token
        else:
            token_getter = lambda: self._current_token
        
        # The parent constructor requires client_id and client_secret, but when
        # using _token_getter_override, the OAuth flow is bypassed.
        super().__init__(
            client_id=client_id or "wrapper-managed",
            client_secret=client_secret or "wrapper-managed",
            _token_getter_override=token_getter,
            **kwargs
        )
    
    async def initialize(self) -> None:
        """Generate token if username/password was provided."""
        if self._username and self._password:
            token = await self._generate_token()
            self._current_token = token
    
    async def _generate_token(self) -> str:
        """Generate token using the auth client."""
        if self._base_url is None:
            raise ValueError("Base URL must be provided")
        
        # Create a simple client wrapper without authentication
        client_wrapper = AsyncClientWrapper(
            base_url=self._base_url,
            httpx_client=httpx.AsyncClient()
        )
        
        # Create the auth client using the existing SDK
        auth_client = AsyncAuthtokenClient(client_wrapper=client_wrapper)
        
        if self._username is None or self._password is None:
            raise ValueError("Username and password must be provided")
        
        response = await auth_client.auth.generate_token(username=self._username, password=self._password)
        return response.token
