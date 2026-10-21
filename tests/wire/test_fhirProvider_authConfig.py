import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.fhir_provider import (
    BadRequestError,
    FhirProviderAddAuthConfigRequest_ClientSecret,
    FhirProviderAddAuthConfigRequest_Jwt,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


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


def test_fhirProvider_authConfig_add_throws_bad_request_error() -> None:
    """Test add endpoint error response (BadRequestError) with WireMock"""
    test_id = "fhir_provider.auth_config.add.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.fhir_provider.auth_config.add(
            fhir_provider_id="fhir_provider_id",
            request=FhirProviderAddAuthConfigRequest_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/add-auth-config", None, 1)


def test_fhirProvider_authConfig_add_throws_unauthorized_error() -> None:
    """Test add endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.auth_config.add.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.auth_config.add(
            fhir_provider_id="fhir_provider_id",
            request=FhirProviderAddAuthConfigRequest_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/add-auth-config", None, 1)


def test_fhirProvider_authConfig_add_throws_forbidden_error() -> None:
    """Test add endpoint error response (ForbiddenError) with WireMock"""
    test_id = "fhir_provider.auth_config.add.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.fhir_provider.auth_config.add(
            fhir_provider_id="fhir_provider_id",
            request=FhirProviderAddAuthConfigRequest_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/add-auth-config", None, 1)


def test_fhirProvider_authConfig_add_throws_not_found_error() -> None:
    """Test add endpoint error response (NotFoundError) with WireMock"""
    test_id = "fhir_provider.auth_config.add.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.fhir_provider.auth_config.add(
            fhir_provider_id="fhir_provider_id",
            request=FhirProviderAddAuthConfigRequest_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/add-auth-config", None, 1)


def test_fhirProvider_authConfig_add_throws_internal_server_error() -> None:
    """Test add endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.auth_config.add.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.auth_config.add(
            fhir_provider_id="fhir_provider_id",
            request=FhirProviderAddAuthConfigRequest_Jwt(
                client_id="client_id",
            ),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/add-auth-config", None, 1)


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


def test_fhirProvider_authConfig_set_active_throws_bad_request_error() -> None:
    """Test setActive endpoint error response (BadRequestError) with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.fhir_provider.auth_config.set_active(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/set-active-auth-config", None, 1)


def test_fhirProvider_authConfig_set_active_throws_unauthorized_error() -> None:
    """Test setActive endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.auth_config.set_active(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/set-active-auth-config", None, 1)


def test_fhirProvider_authConfig_set_active_throws_forbidden_error() -> None:
    """Test setActive endpoint error response (ForbiddenError) with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.fhir_provider.auth_config.set_active(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/set-active-auth-config", None, 1)


def test_fhirProvider_authConfig_set_active_throws_not_found_error() -> None:
    """Test setActive endpoint error response (NotFoundError) with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.fhir_provider.auth_config.set_active(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/set-active-auth-config", None, 1)


def test_fhirProvider_authConfig_set_active_throws_internal_server_error() -> None:
    """Test setActive endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.auth_config.set_active.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.auth_config.set_active(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/set-active-auth-config", None, 1)


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


def test_fhirProvider_authConfig_remove_throws_bad_request_error() -> None:
    """Test remove endpoint error response (BadRequestError) with WireMock"""
    test_id = "fhir_provider.auth_config.remove.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.fhir_provider.auth_config.remove(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/remove-auth-config", None, 1)


def test_fhirProvider_authConfig_remove_throws_unauthorized_error() -> None:
    """Test remove endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir_provider.auth_config.remove.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir_provider.auth_config.remove(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/remove-auth-config", None, 1)


def test_fhirProvider_authConfig_remove_throws_forbidden_error() -> None:
    """Test remove endpoint error response (ForbiddenError) with WireMock"""
    test_id = "fhir_provider.auth_config.remove.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.fhir_provider.auth_config.remove(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/remove-auth-config", None, 1)


def test_fhirProvider_authConfig_remove_throws_not_found_error() -> None:
    """Test remove endpoint error response (NotFoundError) with WireMock"""
    test_id = "fhir_provider.auth_config.remove.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.fhir_provider.auth_config.remove(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/remove-auth-config", None, 1)


def test_fhirProvider_authConfig_remove_throws_internal_server_error() -> None:
    """Test remove endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir_provider.auth_config.remove.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir_provider.auth_config.remove(
            fhir_provider_id="fhir_provider_id",
            auth_config_id="auth_config_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/fhir-provider/fhir_provider_id/remove-auth-config", None, 1)
