from .conftest import get_client, verify_request_count


def test_fhirProvider_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "fhir_provider.create.0"
    client = get_client(test_id)
    client.fhir_provider.create(
        name="Epic Sandbox",
        provider="athenahealth",
        base_url="https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4",
        auth={"auth_method": "jwt", "client_id": "your-client-id"},
    )
    verify_request_count(test_id, "POST", "/fhir-provider", None, 1)


def test_fhirProvider_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "fhir_provider.list_.0"
    client = get_client(test_id)
    client.fhir_provider.list()
    verify_request_count(test_id, "GET", "/fhir-provider/list", None, 1)


def test_fhirProvider_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "fhir_provider.get.0"
    client = get_client(test_id)
    client.fhir_provider.get(fhir_provider_id="fhir_provider_id")
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fhir_provider.delete.0"
    client = get_client(test_id)
    client.fhir_provider.delete(fhir_provider_id="fhir_provider_id")
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_add_auth_config() -> None:
    """Test addAuthConfig endpoint with WireMock"""
    test_id = "fhir_provider.add_auth_config.0"
    client = get_client(test_id)
    client.fhir_provider.add_auth_config(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
        request={"auth_method": "jwt", "client_id": "your-client-id"},
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/add-auth-config", None, 1
    )


def test_fhirProvider_set_active_auth_config() -> None:
    """Test setActiveAuthConfig endpoint with WireMock"""
    test_id = "fhir_provider.set_active_auth_config.0"
    client = get_client(test_id)
    client.fhir_provider.set_active_auth_config(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad", auth_config_id="auth-config-123"
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/set-active-auth-config", None, 1
    )


def test_fhirProvider_remove_auth_config() -> None:
    """Test removeAuthConfig endpoint with WireMock"""
    test_id = "fhir_provider.remove_auth_config.0"
    client = get_client(test_id)
    client.fhir_provider.remove_auth_config(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad", auth_config_id="auth-config-123"
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/remove-auth-config", None, 1
    )
