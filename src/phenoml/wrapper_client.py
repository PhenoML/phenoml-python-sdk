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
        
        # Call parent constructor with the resolved token and all kwargs
        super().__init__(token=token, **kwargs)
    
    def _generate_token(self, username: str, password: str, base_url: str) -> str:
        """Generate token using the auth client."""
        # Create a simple client wrapper without authentication
        client_wrapper = SyncClientWrapper(
            token="",  # No auth needed since we're using basic auth in the request
            base_url=base_url,
            httpx_client=httpx.Client()
        )
        
        # Create the auth client using the existing SDK
        auth_client = AuthtokenClient(client_wrapper=client_wrapper)
        
        print(f"Generating token for {username} using auth client")
        response = auth_client.auth.generate_token(username=username, password=password)
        print(f"Token response: {response}")
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
        if self._base_url is None:
            raise ValueError("Must provide 'base_url' when using username/password")
        
        # Create with temporary token if needed
        super().__init__(token=token or (lambda: ""), **kwargs)
    
    async def initialize(self) -> None:
        """Generate token if username/password was provided."""
        if self._username and self._password:
            token = await self._generate_token()
            # Update the token on the existing instance instead of recreating
            # This is a workaround since we can't easily recreate the instance
            self._token = token
    
    async def _generate_token(self) -> str:
        """Generate token using the auth client."""
        # Ensure base_url is a string
        if self._base_url is None:
            raise ValueError("Base URL must be provided")
        
        # Create a simple client wrapper without authentication
        client_wrapper = AsyncClientWrapper(
            token="",  # No auth needed since we're using basic auth in the request
            base_url=self._base_url,
            httpx_client=httpx.AsyncClient()
        )
        
        # Create the auth client using the existing SDK
        auth_client = AsyncAuthtokenClient(client_wrapper=client_wrapper)
        
        if self._username is None or self._password is None:
            raise ValueError("Username and password must be provided")
        
        response = await auth_client.auth.generate_token(username=self._username, password=self._password)
        return response.token 