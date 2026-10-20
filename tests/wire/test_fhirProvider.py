import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.fhir_provider import (
    BadRequestError,
    FhirProviderCreateRequestAuth_ClientSecret,
    FhirProviderCreateRequestAuth_Jwt,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


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


def test_fhirProvider_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "fhir_provider.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.fhir_provider.create(
            name="x",
            provider="aidbox",
            base_url="base_url",
            auth=FhirProviderCreateRequestAuth_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir-provider", None, 1)


def test_fhirProvider_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.create(
            name="x",
            provider="aidbox",
            base_url="base_url",
            auth=FhirProviderCreateRequestAuth_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir-provider", None, 1)


def test_fhirProvider_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "fhir_provider.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.fhir_provider.create(
            name="x",
            provider="aidbox",
            base_url="base_url",
            auth=FhirProviderCreateRequestAuth_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir-provider", None, 1)


def test_fhirProvider_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.create(
            name="x",
            provider="aidbox",
            base_url="base_url",
            auth=FhirProviderCreateRequestAuth_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir-provider", None, 1)


def test_fhirProvider_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "fhir_provider.list_.0"
    client = get_client(test_id)
    client.fhir_provider.list()
    verify_request_count(test_id, "GET", "/fhir-provider/list", None, 1)


def test_fhirProvider_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir-provider/list", None, 1)


def test_fhirProvider_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.list_.2"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir-provider/list", None, 1)


def test_fhirProvider_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "fhir_provider.get.0"
    client = get_client(test_id)
    client.fhir_provider.get(
        fhir_provider_id="fhir_provider_id",
    )
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.get(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "fhir_provider.get.2"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.fhir_provider.get(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.get.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.get(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fhir_provider.delete.0"
    client = get_client(test_id)
    client.fhir_provider.delete(
        fhir_provider_id="fhir_provider_id",
    )
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.delete(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "fhir_provider.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.fhir_provider.delete(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "fhir_provider.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.fhir_provider.delete(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)


def test_fhirProvider_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.delete(
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir-provider/fhir_provider_id", None, 1)
