from .conftest import get_client, verify_request_count


def test_tools_mcpTools_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "tools.mcp_tools.list_.0"
    client = get_client(test_id)
    client.tools.mcp_tools.list(
        mcp_server_id="mcp_server_id",
    )
    verify_request_count(test_id, "GET", "/tools/mcp-server/mcp_server_id/list", None, 1)


def test_tools_mcpTools_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "tools.mcp_tools.get.0"
    client = get_client(test_id)
    client.tools.mcp_tools.get(
        mcp_server_tool_id="mcp_server_tool_id",
    )
    verify_request_count(test_id, "GET", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)


def test_tools_mcpTools_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "tools.mcp_tools.delete.0"
    client = get_client(test_id)
    client.tools.mcp_tools.delete(
        mcp_server_tool_id="mcp_server_tool_id",
    )
    verify_request_count(test_id, "DELETE", "/tools/mcp-server/tool/mcp_server_tool_id", None, 1)
