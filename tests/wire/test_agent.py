from .conftest import get_client, verify_request_count


def test_agent_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "agent.create.0"
    client = get_client(test_id)
    client.agent.create(name="name", prompts=["prompt_123", "prompt_456"], provider="provider")
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.list_.0"
    client = get_client(test_id)
    client.agent.list(tags="tags")
    verify_request_count(test_id, "GET", "/agent/list", {"tags": "tags"}, 1)


def test_agent_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.get.0"
    client = get_client(test_id)
    client.agent.get(id="id")
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "agent.update.0"
    client = get_client(test_id)
    client.agent.update(id="id", name="name", prompts=["prompt_123", "prompt_456"], provider="provider")
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.delete.0"
    client = get_client(test_id)
    client.agent.delete(id="id")
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "agent.patch.0"
    client = get_client(test_id)
    client.agent.patch(
        id="id",
        request=[
            {"op": "replace", "path": "/name", "value": "Updated Agent Name"},
            {"op": "add", "path": "/tags/-", "value": "new-tag"},
            {"op": "remove", "path": "/description"},
        ],
    )
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)


def test_agent_chat() -> None:
    """Test chat endpoint with WireMock"""
    test_id = "agent.chat.0"
    client = get_client(test_id)
    client.agent.chat(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        message="What is the patient's current condition?",
        agent_id="agent-123",
    )
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_stream_chat() -> None:
    """Test streamChat endpoint with WireMock"""
    test_id = "agent.stream_chat.0"
    client = get_client(test_id)
    for _ in client.agent.stream_chat(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        message="What is the patient's current condition?",
        agent_id="agent-123",
    ):
        pass
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_get_chat_messages() -> None:
    """Test getChatMessages endpoint with WireMock"""
    test_id = "agent.get_chat_messages.0"
    client = get_client(test_id)
    client.agent.get_chat_messages(chat_session_id="chat_session_id", num_messages=1, role="user", order="asc")
    verify_request_count(
        test_id,
        "GET",
        "/agent/chat/messages",
        {"chat_session_id": "chat_session_id", "num_messages": "1", "role": "user", "order": "asc"},
        1,
    )
