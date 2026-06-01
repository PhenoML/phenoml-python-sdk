from .conftest import get_client, verify_request_count

from phenoml.agent import JsonPatchOperation


def test_agent_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "agent.create.0"
    client = get_client(test_id)
    client.agent.create(
        name="Medical Assistant",
        description="An AI assistant for medical information processing",
        prompts=["prompt_123"],
        tags=["medical", "fhir"],
        provider="7002b0b4-8d09-445a-bf65-0fafdaf26c35",
    )
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.list_.0"
    client = get_client(test_id)
    client.agent.list(
        tags="tags",
    )
    verify_request_count(test_id, "GET", "/agent/list", {"tags": "tags"}, 1)


def test_agent_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.get.0"
    client = get_client(test_id)
    client.agent.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "agent.update.0"
    client = get_client(test_id)
    client.agent.update(
        id="id",
        name="Medical Assistant",
        description="Updated description for the medical assistant",
        prompts=["prompt_123"],
        tags=["medical", "fhir", "updated"],
        provider="7002b0b4-8d09-445a-bf65-0fafdaf26c35",
    )
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.delete.0"
    client = get_client(test_id)
    client.agent.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "agent.patch.0"
    client = get_client(test_id)
    client.agent.patch(
        id="id",
        request=[
            JsonPatchOperation(
                op="replace",
                path="/description",
                value="patched description",
            ),
            JsonPatchOperation(
                op="add",
                path="/tags/-",
                value="updated",
            ),
        ],
    )
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)
