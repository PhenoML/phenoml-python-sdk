import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.profiles import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


def test_profiles_versions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "profiles.versions.list_.0"
    client = get_client(test_id)
    client.profiles.versions.list(
        id="custom-patient",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient/versions", None, 1)


def test_profiles_versions_list__throws_bad_request_error() -> None:
    """Test list endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.versions.list_.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.versions.list(
            id="id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.versions.list_.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.versions.list(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.versions.list_.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.versions.list(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_list__throws_not_found_error() -> None:
    """Test list endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.versions.list_.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.versions.list(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.versions.list_.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.versions.list(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "profiles.versions.create.0"
    client = get_client(test_id)
    client.profiles.versions.create(
        id="custom-patient",
        request={"key": "value"},
    )
    verify_request_count(test_id, "POST", "/fhir/profiles/custom-patient/versions", None, 1)


def test_profiles_versions_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.versions.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.versions.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.versions.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create_throws_not_found_error() -> None:
    """Test create endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.versions.create.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create_throws_conflict_error() -> None:
    """Test create endpoint error response (ConflictError) with WireMock"""
    test_id = "profiles.versions.create.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.versions.create.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.versions.create(
            id="id",
            request={"string": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles/id/versions", None, 1)


def test_profiles_versions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "profiles.versions.get.0"
    client = get_client(test_id)
    client.profiles.versions.get(
        id="custom-patient",
        version="2.0.0",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient/versions/2.0.0", None, 1)


def test_profiles_versions_get_throws_bad_request_error() -> None:
    """Test get endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.versions.get.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.versions.get(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.versions.get.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.versions.get(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.versions.get.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.versions.get(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.versions.get.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.versions.get(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.versions.get.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.versions.get(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "profiles.versions.delete.0"
    client = get_client(test_id)
    client.profiles.versions.delete(
        id="custom-patient",
        version="2.0.0",
    )
    verify_request_count(test_id, "DELETE", "/fhir/profiles/custom-patient/versions/2.0.0", None, 1)


def test_profiles_versions_delete_throws_bad_request_error() -> None:
    """Test delete endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.versions.delete.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.versions.delete.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.versions.delete.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.versions.delete.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete_throws_conflict_error() -> None:
    """Test delete endpoint error response (ConflictError) with WireMock"""
    test_id = "profiles.versions.delete.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)


def test_profiles_versions_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.versions.delete.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.versions.delete(
            id="id",
            version="version",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id/versions/version", None, 1)
