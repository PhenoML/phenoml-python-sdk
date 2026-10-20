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


def test_agent_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.create(
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.create(
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.create(
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.create(
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/agent/create", None, 1)


def test_agent_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agent.list_.0"
    client = get_client(test_id)
    client.agent.list(
        tags="tags",
    )
    verify_request_count(test_id, "GET", "/agent/list", {"tags": "tags"}, 1)


def test_agent_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/list", None, 1)


def test_agent_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/list", None, 1)


def test_agent_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/list", None, 1)


def test_agent_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "agent.get.0"
    client = get_client(test_id)
    client.agent.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.get(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.get(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.get(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/agent/id", None, 1)


def test_agent_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.get(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.update(
            id="id",
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.update(
            id="id",
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.update(
            id="id",
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_update_throws_not_found_error() -> None:
    """Test update endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.update.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.update(
            id="id",
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.update.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.update(
            id="id",
            name="name",
            prompts=["prompts", "prompts"],
            provider="provider",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/agent/id", None, 1)


def test_agent_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agent.delete.0"
    client = get_client(test_id)
    client.agent.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.delete(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.delete(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.delete(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/agent/id", None, 1)


def test_agent_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.delete(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_agent_patch_throws_bad_request_error() -> None:
    """Test patch endpoint error response (BadRequestError) with WireMock"""
    test_id = "agent.patch.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.agent.patch(
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
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)


def test_agent_patch_throws_unauthorized_error() -> None:
    """Test patch endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "agent.patch.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.agent.patch(
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
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)


def test_agent_patch_throws_forbidden_error() -> None:
    """Test patch endpoint error response (ForbiddenError) with WireMock"""
    test_id = "agent.patch.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.agent.patch(
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
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)


def test_agent_patch_throws_not_found_error() -> None:
    """Test patch endpoint error response (NotFoundError) with WireMock"""
    test_id = "agent.patch.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.agent.patch(
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
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)


def test_agent_patch_throws_internal_server_error() -> None:
    """Test patch endpoint error response (InternalServerError) with WireMock"""
    test_id = "agent.patch.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.agent.patch(
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
    verify_request_count(test_id, "PATCH", "/agent/id", None, 1)
