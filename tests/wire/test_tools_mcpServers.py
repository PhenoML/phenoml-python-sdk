import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.tools import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError


def test_tools_mcpServers_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "tools.mcp_servers.create.0"
    client = get_client(test_id)
    client.tools.mcp_servers.create(
        name="My MCP Server",
        mcp_server_url="https://mcp.example.com",
    )
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServers_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "tools.mcp_servers.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tools.mcp_servers.create(
            name="name",
            mcp_server_url="mcp_server_url",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServers_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_servers.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_servers.create(
            name="name",
            mcp_server_url="mcp_server_url",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServers_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_servers.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_servers.create(
            name="name",
            mcp_server_url="mcp_server_url",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServers_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_servers.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_servers.create(
            name="name",
            mcp_server_url="mcp_server_url",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServers_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "tools.mcp_servers.list_.0"
    client = get_client(test_id)
    client.tools.mcp_servers.list()
    verify_request_count(test_id, "GET", "/tools/mcp-server/list", None, 1)


def test_tools_mcpServers_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_servers.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_servers.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/list", None, 1)


def test_tools_mcpServers_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_servers.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_servers.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/list", None, 1)


def test_tools_mcpServers_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_servers.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_servers.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/list", None, 1)


def test_tools_mcpServers_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "tools.mcp_servers.get.0"
    client = get_client(test_id)
    client.tools.mcp_servers.get(
        mcp_server_id="mcp_server_id",
    )
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_servers.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_servers.get(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_servers.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_servers.get(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "tools.mcp_servers.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.tools.mcp_servers.get(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_servers.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_servers.get(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "tools.mcp_servers.delete.0"
    client = get_client(test_id)
    client.tools.mcp_servers.delete(
        mcp_server_id="mcp_server_id",
    )
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.mcp_servers.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.mcp_servers.delete(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.mcp_servers.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.mcp_servers.delete(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "tools.mcp_servers.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.tools.mcp_servers.delete(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServers_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.mcp_servers.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.mcp_servers.delete(
            mcp_server_id="mcp_server_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)
