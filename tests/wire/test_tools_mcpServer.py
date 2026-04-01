from .conftest import get_client, verify_request_count


def test_tools_mcpServer_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "tools.mcp_server.create.0"
    client = get_client(test_id)
    client.tools.mcp_server.create(name="My MCP Server", mcp_server_url="https://mcp.example.com")
    verify_request_count(test_id, "POST", "/tools/mcp-server/create", None, 1)


def test_tools_mcpServer_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "tools.mcp_server.list_.0"
    client = get_client(test_id)
    client.tools.mcp_server.list()
    verify_request_count(test_id, "GET", "/tools/mcp-server/list", None, 1)


def test_tools_mcpServer_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "tools.mcp_server.get.0"
    client = get_client(test_id)
    client.tools.mcp_server.get(mcp_server_id="mcp_server_id")
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id", None, 1)


def test_tools_mcpServer_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "tools.mcp_server.delete.0"
    client = get_client(test_id)
    client.tools.mcp_server.delete(mcp_server_id="mcp_server_id")
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/mcp_server_id", None, 1)
