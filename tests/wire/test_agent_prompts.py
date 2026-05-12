from .conftest import get_client, verify_request_count

from phenoml.agent import JsonPatchOperation


def test_agent_prompts_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "agent.prompts.create.0"
    client = get_client(test_id)
    client.agent.prompts.create(
        name="Medical Assistant System Prompt",
        description="System prompt for medical assistant agent",
        content="You are a helpful medical assistant specialized in FHIR data processing.",
        is_default=False,
        tags=["medical", "system"],
    )
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_prompts_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.prompts.list_.0"
    client = get_client(test_id)
    client.agent.prompts.list()
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_prompts_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.prompts.get.0"
    client = get_client(test_id)
    client.agent.prompts.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_prompts_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "agent.prompts.update.0"
    client = get_client(test_id)
    client.agent.prompts.update(
        id="id",
        name="Medical Assistant System Prompt",
        description="Updated system prompt",
        content="You are a helpful medical assistant. Always cite ICD-10 codes when discussing diagnoses.",
        is_default=False,
        tags=["medical", "system", "updated"],
    )
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.prompts.delete.0"
    client = get_client(test_id)
    client.agent.prompts.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_prompts_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "agent.prompts.patch.0"
    client = get_client(test_id)
    client.agent.prompts.patch(
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


def test_agent_prompts_load_defaults() -> None:
    """Test loadDefaults endpoint with WireMock"""
    test_id = "agent.prompts.load_defaults.0"
    client = get_client(test_id)
    client.agent.prompts.load_defaults()
    verify_request_count(test_id, "POST", "/agent/prompts/load-defaults", None, 1)
