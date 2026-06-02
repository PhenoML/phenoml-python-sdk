from .conftest import get_client, verify_request_count

from phenoml.fhir_provider import FhirProviderCreateRequestAuth_ClientSecret


def test_fhirProvider_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "fhir_provider.create.0"
    client = get_client(test_id)
    client.fhir_provider.create(
        name="Epic Sandbox",
        description="Epic sandbox environment for testing",
        provider="epic",
        base_url="https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4",
        auth=FhirProviderCreateRequestAuth_ClientSecret(
            client_id="your-client-id",
            client_secret="your-client-secret",
        ),
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
    client.fhir_provider.get(
        fhir_provider_id="fhir_provider_id",
    )
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fhir_provider.delete.0"
    client = get_client(test_id)
    client.fhir_provider.delete(
        fhir_provider_id="fhir_provider_id",
    )
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)
