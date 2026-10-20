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


def test_profiles_profiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "profiles.profiles.list_.0"
    client = get_client(test_id)
    client.profiles.profiles.list(
        url="http://phenoml.com/fhir/StructureDefinition/custom-patient|1.0.0",
    )
    verify_request_count(
        test_id, "GET", "/fhir/profiles", {"url": "http://phenoml.com/fhir/StructureDefinition/custom-patient|1.0.0"}, 1
    )


def test_profiles_profiles_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.profiles.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.profiles.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles", None, 1)


def test_profiles_profiles_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.profiles.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.profiles.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles", None, 1)


def test_profiles_profiles_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.profiles.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.profiles.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles", None, 1)


def test_profiles_profiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "profiles.profiles.create.0"
    client = get_client(test_id)
    client.profiles.profiles.create(
        structure_definition={
            "resourceType": "StructureDefinition",
            "id": "custom-patient",
            "url": "http://phenoml.com/fhir/StructureDefinition/custom-patient",
            "name": "CustomPatient",
            "status": "active",
            "fhirVersion": "4.0.1",
            "kind": "resource",
            "abstract": False,
            "type": "Patient",
            "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Patient",
            "derivation": "constraint",
            "snapshot": {"element": [{"id": "Patient", "path": "Patient", "min": 0, "max": "*"}]},
        },
        implementation_guide="acme-cardiology",
    )
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.profiles.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.profiles.create(
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.profiles.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.profiles.create(
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.profiles.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.profiles.create(
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.profiles.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.profiles.create(
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "profiles.profiles.get.0"
    client = get_client(test_id)
    client.profiles.profiles.get(
        id="custom-patient",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient", None, 1)


def test_profiles_profiles_get_throws_bad_request_error() -> None:
    """Test get endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.profiles.get.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.profiles.get(
            id="id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.profiles.get.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.profiles.get(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.profiles.get.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.profiles.get(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.profiles.get.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.profiles.get(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.profiles.get.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.profiles.get(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "profiles.profiles.update.0"
    client = get_client(test_id)
    client.profiles.profiles.update(
        id="custom-patient",
        structure_definition={
            "resourceType": "StructureDefinition",
            "id": "custom-patient",
            "url": "http://phenoml.com/fhir/StructureDefinition/custom-patient",
            "name": "CustomPatient",
            "status": "active",
            "fhirVersion": "4.0.1",
            "kind": "resource",
            "abstract": False,
            "type": "Patient",
            "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Patient",
            "derivation": "constraint",
            "snapshot": {"element": [{"id": "Patient", "path": "Patient", "min": 0, "max": "*"}]},
        },
        implementation_guide="acme-cardiology",
    )
    verify_request_count(test_id, "PUT", "/fhir/profiles/custom-patient", None, 1)


def test_profiles_profiles_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.profiles.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.profiles.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.profiles.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update_throws_not_found_error() -> None:
    """Test update endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.profiles.update.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update_throws_conflict_error() -> None:
    """Test update endpoint error response (ConflictError) with WireMock"""
    test_id = "profiles.profiles.update.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.profiles.update.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.profiles.update(
            id="id",
            structure_definition={"structure_definition": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "profiles.profiles.delete.0"
    client = get_client(test_id)
    client.profiles.profiles.delete(
        id="custom-patient",
    )
    verify_request_count(test_id, "DELETE", "/fhir/profiles/custom-patient", None, 1)


def test_profiles_profiles_delete_throws_bad_request_error() -> None:
    """Test delete endpoint error response (BadRequestError) with WireMock"""
    test_id = "profiles.profiles.delete.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "profiles.profiles.delete.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "profiles.profiles.delete.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "profiles.profiles.delete.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete_throws_conflict_error() -> None:
    """Test delete endpoint error response (ConflictError) with WireMock"""
    test_id = "profiles.profiles.delete.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)


def test_profiles_profiles_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "profiles.profiles.delete.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.profiles.profiles.delete(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/profiles/id", None, 1)
