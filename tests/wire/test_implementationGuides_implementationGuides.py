import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.implementation_guides import (
    BadRequestError,
    ConflictError,
    FhirImplementationGuide,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


def test_implementationGuides_implementationGuides_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.list_.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.list()
    verify_request_count(test_id, "GET", "/fhir/implementation-guides", None, 1)


def test_implementationGuides_implementationGuides_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.implementation_guides.implementation_guides.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides", None, 1)


def test_implementationGuides_implementationGuides_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.implementation_guides.implementation_guides.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides", None, 1)


def test_implementationGuides_implementationGuides_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.implementation_guides.implementation_guides.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides", None, 1)


def test_implementationGuides_implementationGuides_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.get(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_get_throws_bad_request_error() -> None:
    """Test get endpoint error response (BadRequestError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.implementation_guides.implementation_guides.get(
            name="name",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.implementation_guides.implementation_guides.get(
            name="name",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.implementation_guides.implementation_guides.get(
            name="name",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.implementation_guides.implementation_guides.get(
            name="name",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.implementation_guides.implementation_guides.get(
            name="name",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.update(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.implementation_guides.implementation_guides.update(
            name="name",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.implementation_guides.implementation_guides.update(
            name="name",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.implementation_guides.implementation_guides.update(
            name="name",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.implementation_guides.implementation_guides.update(
            name="name",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.delete(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_delete_throws_bad_request_error() -> None:
    """Test delete endpoint error response (BadRequestError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.implementation_guides.implementation_guides.delete(
            name="name",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.implementation_guides.implementation_guides.delete(
            name="name",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.implementation_guides.implementation_guides.delete(
            name="name",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.implementation_guides.implementation_guides.delete(
            name="name",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.implementation_guides.implementation_guides.delete(
            name="name",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/name", None, 1)


def test_implementationGuides_implementationGuides_create_version() -> None:
    """Test createVersion endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.create_version.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.create_version(
        name="name",
        implementation_guide=FhirImplementationGuide(
            resource_type="ImplementationGuide",
            url="url",
            version="version",
        ),
        profile_refs=["profile_refs"],
    )
    verify_request_count(test_id, "POST", "/fhir/implementation-guides/name/versions", None, 1)


def test_implementationGuides_implementationGuides_create_version_throws_bad_request_error() -> None:
    """Test createVersion endpoint error response (BadRequestError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.create_version.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.implementation_guides.implementation_guides.create_version(
            name="name",
            implementation_guide=FhirImplementationGuide(
                resource_type="ImplementationGuide",
                url="url",
                version="version",
            ),
            profile_refs=["profile_refs", "profile_refs"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/implementation-guides/name/versions", None, 1)


def test_implementationGuides_implementationGuides_create_version_throws_not_found_error() -> None:
    """Test createVersion endpoint error response (NotFoundError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.create_version.2"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.implementation_guides.implementation_guides.create_version(
            name="name",
            implementation_guide=FhirImplementationGuide(
                resource_type="ImplementationGuide",
                url="url",
                version="version",
            ),
            profile_refs=["profile_refs", "profile_refs"],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/implementation-guides/name/versions", None, 1)


def test_implementationGuides_implementationGuides_create_version_throws_conflict_error() -> None:
    """Test createVersion endpoint error response (ConflictError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.create_version.3"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.implementation_guides.implementation_guides.create_version(
            name="name",
            implementation_guide=FhirImplementationGuide(
                resource_type="ImplementationGuide",
                url="url",
                version="version",
            ),
            profile_refs=["profile_refs", "profile_refs"],
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir/implementation-guides/name/versions", None, 1)


def test_implementationGuides_implementationGuides_get_version() -> None:
    """Test getVersion endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.get_version.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.get_version(
        name="name",
        version="1.0.0",
    )
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name/versions/1.0.0", None, 1)


def test_implementationGuides_implementationGuides_get_version_throws_bad_request_error() -> None:
    """Test getVersion endpoint error response (BadRequestError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get_version.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.implementation_guides.implementation_guides.get_version(
            name="name",
            version="version",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name/versions/version", None, 1)


def test_implementationGuides_implementationGuides_get_version_throws_not_found_error() -> None:
    """Test getVersion endpoint error response (NotFoundError) with WireMock"""
    test_id = "implementation_guides.implementation_guides.get_version.2"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.implementation_guides.implementation_guides.get_version(
            name="name",
            version="version",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name/versions/version", None, 1)
