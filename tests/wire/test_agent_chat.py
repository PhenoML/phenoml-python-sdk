import pytest
from .conftest import get_client, verify_request_count

from phenoml.agent import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)
from phenoml.core.jsonable_encoder import jsonable_encoder


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


def test_agent_chat_send_create_clinical_resources() -> None:
    """Test send endpoint (Create Clinical Resources example) with WireMock"""
    test_id = "agent.chat.send.1"
    client = get_client(test_id)
    client.agent.chat.send(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        message="Create a patient record for Jane Doe, 32F, diagnosed with iron deficiency anemia. Prescribe ferrous sulfate 325mg daily.",
        session_id="session-def456",
        agent_id="agent-123",
        enhanced_reasoning=True,
    )
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_bad_request_error() -> None:
    """Test send endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.chat.send.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_unauthorized_error() -> None:
    """Test send endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.chat.send.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_forbidden_error() -> None:
    """Test send endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.chat.send.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_not_found_error() -> None:
    """Test send endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.chat.send.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_conflict_error() -> None:
    """Test send endpoint error response (ConflictError) with WireMock"""
    test_id = "agent.chat.send.6"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_internal_server_error() -> None:
    """Test send endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.chat.send.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/chat", None, 1)


def test_agent_chat_send_throws_gateway_timeout_error() -> None:
    """Test send endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "agent.chat.send.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.agent.chat.send(
            message="message",
            agent_id="agent_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_chat_stream_throws_bad_request_error() -> None:
    """Test stream endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.chat.stream.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_unauthorized_error() -> None:
    """Test stream endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.chat.stream.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_forbidden_error() -> None:
    """Test stream endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.chat.stream.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_not_found_error() -> None:
    """Test stream endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.chat.stream.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_conflict_error() -> None:
    """Test stream endpoint error response (ConflictError) with WireMock"""
    test_id = "agent.chat.stream.5"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_internal_server_error() -> None:
    """Test stream endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.chat.stream.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/stream-chat", None, 1)


def test_agent_chat_stream_throws_gateway_timeout_error() -> None:
    """Test stream endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "agent.chat.stream.7"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        for _ in client.agent.chat.stream(
            message="message",
            agent_id="agent_id",
        ):
            pass
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_chat_list_messages_throws_unauthorized_error() -> None:
    """Test listMessages endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.chat.list_messages.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.chat.list_messages(
            chat_session_id="chat_session_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/chat/messages", {"chat_session_id": "chat_session_id"}, 1)


def test_agent_chat_list_messages_throws_forbidden_error() -> None:
    """Test listMessages endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.chat.list_messages.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.chat.list_messages(
            chat_session_id="chat_session_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/chat/messages", {"chat_session_id": "chat_session_id"}, 1)


def test_agent_chat_list_messages_throws_not_found_error() -> None:
    """Test listMessages endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.chat.list_messages.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.chat.list_messages(
            chat_session_id="chat_session_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/chat/messages", {"chat_session_id": "chat_session_id"}, 1)


def test_agent_chat_list_messages_throws_internal_server_error() -> None:
    """Test listMessages endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.chat.list_messages.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.chat.list_messages(
            chat_session_id="chat_session_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/chat/messages", {"chat_session_id": "chat_session_id"}, 1)


def test_agent_chat_list_messages_throws_gateway_timeout_error() -> None:
    """Test listMessages endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "agent.chat.list_messages.5"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.agent.chat.list_messages(
            chat_session_id="chat_session_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/chat/messages", {"chat_session_id": "chat_session_id"}, 1)
