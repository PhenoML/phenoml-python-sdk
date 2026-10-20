import pytest
from .conftest import get_client, verify_request_count

from phenoml.agent import (
    BadRequestError,
    ForbiddenError,
    InternalServerError,
    JsonPatchOperation,
    NotFoundError,
    UnauthorizedError,
)
from phenoml.core.jsonable_encoder import jsonable_encoder


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


def test_agent_prompts_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.prompts.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.prompts.create(
            name="name",
            content="content",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_prompts_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.create(
            name="name",
            content="content",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_prompts_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.create(
            name="name",
            content="content",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_prompts_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.create(
            name="name",
            content="content",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/prompts", None, 1)


def test_agent_prompts_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.prompts.list_.0"
    client = get_client(test_id)
    client.agent.prompts.list()
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_prompts_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_prompts_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_prompts_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/list", None, 1)


def test_agent_prompts_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.prompts.get.0"
    client = get_client(test_id)
    client.agent.prompts.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_prompts_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.get(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_prompts_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.get(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_prompts_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.prompts.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.prompts.get(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/prompts/id", None, 1)


def test_agent_prompts_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.get(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_prompts_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.prompts.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.prompts.update(
            id="id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.update(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.update(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_update_throws_not_found_error() -> None:
    """Test update endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.prompts.update.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.prompts.update(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.update.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.update(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.prompts.delete.0"
    client = get_client(test_id)
    client.agent.prompts.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.delete(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.delete(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.prompts.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.prompts.delete(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/prompts/id", None, 1)


def test_agent_prompts_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.delete(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_prompts_patch_throws_bad_request_error() -> None:
    """Test patch endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.prompts.patch.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.prompts.patch(
            id="id",
            request=[
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
            ],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)


def test_agent_prompts_patch_throws_unauthorized_error() -> None:
    """Test patch endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.prompts.patch.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.prompts.patch(
            id="id",
            request=[
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
            ],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)


def test_agent_prompts_patch_throws_forbidden_error() -> None:
    """Test patch endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.prompts.patch.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.prompts.patch(
            id="id",
            request=[
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
            ],
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)


def test_agent_prompts_patch_throws_not_found_error() -> None:
    """Test patch endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.prompts.patch.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.prompts.patch(
            id="id",
            request=[
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
            ],
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)


def test_agent_prompts_patch_throws_internal_server_error() -> None:
    """Test patch endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.prompts.patch.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.prompts.patch(
            id="id",
            request=[
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
                JsonPatchOperation(
                    op="add",
                    path="path",
                ),
            ],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PATCH", "/agent/prompts/id", None, 1)
