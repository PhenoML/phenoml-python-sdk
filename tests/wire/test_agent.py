from .conftest import get_client, verify_request_count

from phenoml.agent import JsonPatchOperation


def test_agent_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "agent.create.0"
    client = get_client(test_id)
    client.agent.create(
        name="Medical Assistant System Prompt",
        description="System prompt for medical assistant agent",
        content="You are a helpful medical assistant specialized in FHIR data processing.",
        is_default=False,
        tags=["medical", "system"],
    )
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.list_.0"
    client = get_client(test_id)
    client.agent.list()
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.get.0"
    client = get_client(test_id)
    client.agent.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "agent.update.0"
    client = get_client(test_id)
    client.agent.update(
        id="id",
        name="Medical Assistant System Prompt",
        description="Updated system prompt",
        content="You are a helpful medical assistant. Always cite ICD-10 codes when discussing diagnoses.",
        is_default=False,
        tags=["medical", "system", "updated"],
    )
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.delete.0"
    client = get_client(test_id)
    client.agent.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "agent.patch.0"
    client = get_client(test_id)
    client.agent.patch(
        id="id",
        request=[
            JsonPatchOperation(
                op="replace",
                path="/content",
                value="Updated prompt content.",
            )
        ],
    )
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)
