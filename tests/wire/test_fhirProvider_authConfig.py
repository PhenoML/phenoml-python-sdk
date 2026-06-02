from .conftest import get_client, verify_request_count

from phenoml.fhir_provider import FhirProviderAddAuthConfigRequest_ClientSecret


def test_fhirProvider_authConfig_add() -> None:
    """Test add endpoint with WireMock"""
    test_id = "fhir_provider.auth_config.add.0"
    client = get_client(test_id)
    client.fhir_provider.auth_config.add(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
        request=FhirProviderAddAuthConfigRequest_ClientSecret(
            client_id="your-client-id",
            client_secret="your-client-secret",
        ),
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/add-auth-config", None, 1
    )


def test_fhirProvider_authConfig_set_active() -> None:
    """Test setActive endpoint with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.0"
    client = get_client(test_id)
    client.fhir_provider.auth_config.set_active(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
        auth_config_id="auth-config-456",
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/set-active-auth-config", None, 1
    )


def test_fhirProvider_authConfig_remove() -> None:
    """Test remove endpoint with WireMock"""
    test_id = "fhir_provider.auth_config.remove.0"
    client = get_client(test_id)
    client.fhir_provider.auth_config.remove(
        fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
        auth_config_id="auth-config-456",
    )
    verify_request_count(
        test_id, "PATCH", "/fhir-provider/1716d214-de93-43a4-aa6b-a878d864e2ad/remove-auth-config", None, 1
    )
