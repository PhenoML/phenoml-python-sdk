from .conftest import get_client, verify_request_count


def test_authtoken_get_token() -> None:
    """Test getToken endpoint with WireMock"""
    test_id = "authtoken.get_token.0"
    client = get_client(test_id)
    client.authtoken.get_token(
        client_id="your_client_id",
        client_secret="your_client_secret",
    )
    verify_request_count(test_id, "POST", "/v2/auth/token", None, 2)
