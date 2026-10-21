import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.tools import ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError


def test_tools_mcpTools_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "tools.mcp_tools.list_.0"
    client = get_client(test_id)
    client.tools.mcp_tools.list(
        mcp_server_id="mcp_server_id",
    )
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id/list", None, 1)


def test_tools_mcpTools_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_tools.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_tools.list(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id/list", None, 1)


def test_tools_mcpTools_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_tools.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_tools.list(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id/list", None, 1)


def test_tools_mcpTools_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_tools.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_tools.list(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id/list", None, 1)


def test_tools_mcpTools_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "tools.mcp_tools.get.0"
    client = get_client(test_id)
    client.tools.mcp_tools.get(
        mcp_server_tool_id="mcp_server_tool_id",
    )
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_tools.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_tools.get(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_tools.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_tools.get(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "tools.mcp_tools.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.tools.mcp_tools.get(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_tools.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_tools.get(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "tools.mcp_tools.delete.0"
    client = get_client(test_id)
    client.tools.mcp_tools.delete(
        mcp_server_tool_id="mcp_server_tool_id",
    )
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_tools.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_tools.delete(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_tools.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_tools.delete(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "tools.mcp_tools.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.tools.mcp_tools.delete(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_tools.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_tools.delete(
            mcp_server_tool_id="mcp_server_tool_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)
