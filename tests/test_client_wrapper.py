from phenoml.core.client_wrapper import BaseClientWrapper


def test_default_headers_include_sdk_versioned_user_agent() -> None:
    client_wrapper = BaseClientWrapper(base_url="https://api.example.com")

    headers = client_wrapper.get_headers()

    assert headers["User-Agent"] == "phenoml/16.6.0"
    assert headers["X-Fern-SDK-Version"] == "16.6.0"
