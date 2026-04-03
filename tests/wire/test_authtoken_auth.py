from .conftest import get_client, verify_request_count


def test_authtoken_auth_get_token() -> None:
    """Test getToken endpoint with WireMock"""
    test_id = "authtoken.auth.get_token.0"
    client = get_client(test_id)
    client.authtoken.auth.get_token()
    verify_request_count(test_id, "POST", "/v2/auth/token", None, 2)
