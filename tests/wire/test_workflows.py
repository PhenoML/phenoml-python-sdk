from .conftest import get_client, verify_request_count


def test_workflows_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "workflows.list_.0"
    client = get_client(test_id)
    client.workflows.list(
        verbose=True,
    )
    verify_request_count(test_id, "GET", "/workflows", {"verbose": "true"}, 1)


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


def test_workflows_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "workflows.get.0"
    client = get_client(test_id)
    client.workflows.get(
        id="id",
        verbose=True,
    )
    verify_request_count(test_id, "GET", "/workflows/id", {"verbose": "true"}, 1)


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


def test_workflows_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "workflows.delete.0"
    client = get_client(test_id)
    client.workflows.delete(
        id="id",
    )
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
