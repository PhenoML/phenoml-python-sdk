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
            token = self._generate_token(username, password, kwargs.get('base_url'))
        
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
        
        # Create with temporary token if needed
        super().__init__(token=token or (lambda: ""), **kwargs)
    
    async def initialize(self) -> None:
        """Generate token if username/password was provided."""
        if self._username and self._password:
            token = await self._generate_token()
            # Recreate with generated token (re-calling __init__ is a workaround for immutable super().__init__ args)
            self.__init__(token=token, base_url=self._base_url)
    
    async def _generate_token(self) -> str:
        """Generate token using the auth client."""
        # Create a simple client wrapper without authentication
        client_wrapper = AsyncClientWrapper(
            token="",  # No auth needed since we're using basic auth in the request
            base_url=self._base_url,
            httpx_client=httpx.AsyncClient()
        )
        
        # Create the auth client using the existing SDK
        auth_client = AsyncAuthtokenClient(client_wrapper=client_wrapper)
        
        response = await auth_client.auth.generate_token(username=self._username, password=self._password)
        return response.token 