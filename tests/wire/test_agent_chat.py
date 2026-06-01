from .conftest import get_client, verify_request_count


def test_agent_chat_send() -> None:
    """Test send endpoint with WireMock"""
    test_id = "agent.chat.send.0"
    client = get_client(test_id)
    client.agent.chat.send(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        message="What is the patient's current condition?",
        session_id="session-abc123",
        agent_id="agent-123",
    )
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_stream() -> None:
    """Test stream endpoint with WireMock"""
    test_id = "agent.chat.stream.0"
    client = get_client(test_id)
    for _ in client.agent.chat.stream(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        message="What is the patient's current condition?",
        session_id="session-abc123",
        agent_id="agent-123",
    ):
        pass
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_list_messages() -> None:
    """Test listMessages endpoint with WireMock"""
    test_id = "agent.chat.list_messages.0"
    client = get_client(test_id)
    client.agent.chat.list_messages(
        chat_session_id="chat_session_id",
        num_messages=1,
        role="user",
        order="asc",
    )
    verify_request_count(
        test_id,
        "GET",
        "/agent/chat/messages",
        {"chat_session_id": "chat_session_id", "num_messages": "1", "role": "user", "order": "asc"},
        1,
    )
