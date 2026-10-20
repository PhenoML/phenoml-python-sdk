import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.workflows import (
    BadRequestError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


def test_workflows_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "workflows.list_.0"
    client = get_client(test_id)
    client.workflows.list(
        verbose=True,
    )
    verify_request_count(test_id, "GET", "/workflows", {"verbose": "true"}, 1)


def test_workflows_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows", None, 1)


def test_workflows_list__throws_forbidden_error() -> None:
    """Test list endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.list_.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.list()
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows", None, 1)


def test_workflows_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.list_.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows", None, 1)


def test_workflows_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "workflows.create.0"
    client = get_client(test_id)
    client.workflows.create(
        verbose=True,
        name="Patient Data Mapping Workflow",
        workflow_instructions="Given diagnosis data, find the patient and create a condition record linked to their encounter",
        sample_data={
            "patient_last_name": "Rippin",
            "patient_first_name": "Clay",
            "diagnosis_code": "I10",
            "encounter_date": "2024-01-15",
        },
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    )
    verify_request_count(test_id, "POST", "/workflows", {"verbose": "true"}, 1)


def test_workflows_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "workflows.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.workflows.create(
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows", None, 1)


def test_workflows_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.create(
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows", None, 1)


def test_workflows_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.create.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.create(
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows", None, 1)


def test_workflows_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.create(
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows", None, 1)


def test_workflows_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "workflows.get.0"
    client = get_client(test_id)
    client.workflows.get(
        id="id",
        verbose=True,
    )
    verify_request_count(test_id, "GET", "/workflows/id", {"verbose": "true"}, 1)


def test_workflows_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.get(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows/id", None, 1)


def test_workflows_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.get(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows/id", None, 1)


def test_workflows_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "workflows.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.workflows.get(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows/id", None, 1)


def test_workflows_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.get(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows/id", None, 1)


def test_workflows_get_throws_gateway_timeout_error() -> None:
    """Test get endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "workflows.get.5"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.workflows.get(
            id="id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/workflows/id", None, 1)


def test_workflows_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "workflows.update.0"
    client = get_client(test_id)
    client.workflows.update(
        id="id",
        verbose=True,
        name="Patient Data Mapping Workflow (v2)",
        workflow_instructions="Given diagnosis data, find the patient and create a condition record linked to their encounter",
        sample_data={
            "patient_last_name": "Rippin",
            "patient_first_name": "Clay",
            "diagnosis_code": "I10",
            "encounter_date": "2024-01-15",
        },
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    )
    verify_request_count(test_id, "PUT", "/workflows/id", {"verbose": "true"}, 1)


def test_workflows_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "workflows.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_update_throws_not_found_error() -> None:
    """Test update endpoint error response (NotFoundError) with WireMock"""
    test_id = "workflows.update.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.update.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_update_throws_gateway_timeout_error() -> None:
    """Test update endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "workflows.update.6"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.workflows.update(
            id="id",
            name="name",
            workflow_instructions="workflow_instructions",
            sample_data={"sample_data": {"key": "value"}},
            fhir_provider_id="fhir_provider_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/workflows/id", None, 1)


def test_workflows_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "workflows.delete.0"
    client = get_client(test_id)
    client.workflows.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.delete(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.delete(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "workflows.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.workflows.delete(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.delete(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_delete_throws_gateway_timeout_error() -> None:
    """Test delete endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "workflows.delete.5"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.workflows.delete(
            id="id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/workflows/id", None, 1)


def test_workflows_execute() -> None:
    """Test execute endpoint with WireMock"""
    test_id = "workflows.execute.0"
    client = get_client(test_id)
    client.workflows.execute(
        id="7a8b9c0d-1234-5678-abcd-ef9876543210",
        input_data={
            "patient_last_name": "Johnson",
            "patient_first_name": "Mary",
            "diagnosis_code": "M79.3",
            "encounter_date": "2024-03-20",
        },
    )
    verify_request_count(test_id, "POST", "/workflows/7a8b9c0d-1234-5678-abcd-ef9876543210/execute", None, 1)


def test_workflows_execute_preview_mode() -> None:
    """Test execute endpoint (Preview Mode example) with WireMock"""
    test_id = "workflows.execute.1"
    client = get_client(test_id)
    client.workflows.execute(
        id="7a8b9c0d-1234-5678-abcd-ef9876543210",
        input_data={"patient_last_name": "Johnson", "patient_first_name": "Mary", "diagnosis_code": "M79.3"},
        preview=True,
    )
    verify_request_count(test_id, "POST", "/workflows/7a8b9c0d-1234-5678-abcd-ef9876543210/execute", None, 1)


def test_workflows_execute_throws_bad_request_error() -> None:
    """Test execute endpoint error response (BadRequestError) with WireMock"""
    test_id = "workflows.execute.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)


def test_workflows_execute_throws_unauthorized_error() -> None:
    """Test execute endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "workflows.execute.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)


def test_workflows_execute_throws_forbidden_error() -> None:
    """Test execute endpoint error response (ForbiddenError) with WireMock"""
    test_id = "workflows.execute.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)


def test_workflows_execute_throws_not_found_error() -> None:
    """Test execute endpoint error response (NotFoundError) with WireMock"""
    test_id = "workflows.execute.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)


def test_workflows_execute_throws_internal_server_error() -> None:
    """Test execute endpoint error response (InternalServerError) with WireMock"""
    test_id = "workflows.execute.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)


def test_workflows_execute_throws_gateway_timeout_error() -> None:
    """Test execute endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "workflows.execute.7"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.workflows.execute(
            id="id",
            input_data={"input_data": {"key": "value"}},
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/workflows/id/execute", None, 1)
