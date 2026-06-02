from .conftest import get_client, verify_request_count

from phenoml.construe import CodeResponse


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


def test_construe_codeSystems_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "construe.code_systems.list_.0"
    client = get_client(test_id)
    client.construe.code_systems.list()
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


def test_construe_codeSystems_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "construe.code_systems.delete.0"
    client = get_client(test_id)
    client.construe.code_systems.delete(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/CUSTOM_CODES", {"version": "version"}, 1)


def test_construe_codeSystems_export() -> None:
    """Test export endpoint with WireMock"""
    test_id = "construe.code_systems.export.0"
    client = get_client(test_id)
    client.construe.code_systems.export(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/systems/CUSTOM_CODES/export", {"version": "version"}, 1)
