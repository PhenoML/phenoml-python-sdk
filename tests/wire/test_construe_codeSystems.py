import pytest
from .conftest import get_client, verify_request_count

from phenoml.construe import (
    BadRequestError,
    CodeResponse,
    ConflictError,
    FailedDependencyError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)
from phenoml.core.jsonable_encoder import jsonable_encoder


def test_construe_codeSystems_upload() -> None:
    """Test upload endpoint with WireMock"""
    test_id = "construe.code_systems.upload.0"
    client = get_client(test_id)
    client.construe.code_systems.upload(
        name="CUSTOM_CODES",
        version="1.0",
        format="json",
        codes=[
            CodeResponse(
                code="X001",
                description="Example custom code 1",
            ),
            CodeResponse(
                code="X002",
                description="Example custom code 2",
            ),
        ],
    )
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_csv_file_base64encoded() -> None:
    """Test upload endpoint (CSV file (base64-encoded) example) with WireMock"""
    test_id = "construe.code_systems.upload.1"
    client = get_client(test_id)
    client.construe.code_systems.upload(
        name="CUSTOM_CODES",
        version="1.0",
        format="csv",
        file="Y29kZSxkZXNjcmlwdGlvbgpYMDAxLEV4YW1wbGUgY3VzdG9tIGNvZGUgMQo=",
        code_col="code",
        desc_col="description",
    )
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_bad_request_error() -> None:
    """Test upload endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.code_systems.upload.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_unauthorized_error() -> None:
    """Test upload endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.code_systems.upload.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_forbidden_error() -> None:
    """Test upload endpoint error response (ForbiddenError) with WireMock"""
    test_id = "construe.code_systems.upload.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_conflict_error() -> None:
    """Test upload endpoint error response (ConflictError) with WireMock"""
    test_id = "construe.code_systems.upload.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_failed_dependency_error() -> None:
    """Test upload endpoint error response (FailedDependencyError) with WireMock"""
    test_id = "construe.code_systems.upload.6"
    client = get_client(test_id)
    with pytest.raises(FailedDependencyError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 424
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_upload_throws_internal_server_error() -> None:
    """Test upload endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.code_systems.upload.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.code_systems.upload(
            name="name",
            version="version",
            format="csv",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_codeSystems_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "construe.code_systems.list_.0"
    client = get_client(test_id)
    client.construe.code_systems.list()
    verify_request_count(test_id, "GET", "/construe/codes/systems", None, 1)


def test_construe_codeSystems_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.code_systems.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.code_systems.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems", None, 1)


def test_construe_codeSystems_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.code_systems.list_.2"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.code_systems.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems", None, 1)


def test_construe_codeSystems_find() -> None:
    """Test find endpoint with WireMock"""
    test_id = "construe.code_systems.find.0"
    client = get_client(test_id)
    client.construe.code_systems.find(
        codesystem="ICD-10-CM",
        version="2025",
    )
    verify_request_count(test_id, "GET", "/construe/codes/systems/ICD-10-CM", {"version": "2025"}, 1)


def test_construe_codeSystems_find_throws_bad_request_error() -> None:
    """Test find endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.code_systems.find.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.code_systems.find(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_find_throws_unauthorized_error() -> None:
    """Test find endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.code_systems.find.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.code_systems.find(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_find_throws_not_found_error() -> None:
    """Test find endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.code_systems.find.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.code_systems.find(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_find_throws_internal_server_error() -> None:
    """Test find endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.code_systems.find.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.code_systems.find(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "construe.code_systems.delete.0"
    client = get_client(test_id)
    client.construe.code_systems.delete(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/CUSTOM_CODES", {"version": "version"}, 1)


def test_construe_codeSystems_delete_throws_bad_request_error() -> None:
    """Test delete endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.code_systems.delete.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.code_systems.delete(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.code_systems.delete.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.code_systems.delete(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "construe.code_systems.delete.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.construe.code_systems.delete(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.code_systems.delete.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.code_systems.delete(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.code_systems.delete.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.code_systems.delete(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/codesystem", None, 1)


def test_construe_codeSystems_export() -> None:
    """Test export endpoint with WireMock"""
    test_id = "construe.code_systems.export.0"
    client = get_client(test_id)
    client.construe.code_systems.export(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/systems/CUSTOM_CODES/export", {"version": "version"}, 1)


def test_construe_codeSystems_export_throws_bad_request_error() -> None:
    """Test export endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.code_systems.export.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_unauthorized_error() -> None:
    """Test export endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.code_systems.export.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_forbidden_error() -> None:
    """Test export endpoint error response (ForbiddenError) with WireMock"""
    test_id = "construe.code_systems.export.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_not_found_error() -> None:
    """Test export endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.code_systems.export.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_conflict_error() -> None:
    """Test export endpoint error response (ConflictError) with WireMock"""
    test_id = "construe.code_systems.export.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_failed_dependency_error() -> None:
    """Test export endpoint error response (FailedDependencyError) with WireMock"""
    test_id = "construe.code_systems.export.6"
    client = get_client(test_id)
    with pytest.raises(FailedDependencyError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 424
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)


def test_construe_codeSystems_export_throws_internal_server_error() -> None:
    """Test export endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.code_systems.export.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.code_systems.export(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/systems/codesystem/export", None, 1)
