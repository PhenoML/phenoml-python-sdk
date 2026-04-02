from .conftest import get_client, verify_request_count

from phenoml.summary import FhirResource


def test_summary_list_templates() -> None:
    """Test listTemplates endpoint with WireMock"""
    test_id = "summary.list_templates.0"
    client = get_client(test_id)
    client.summary.list_templates()
    verify_request_count(test_id, "GET", "/fhir2summary/templates", None, 1)


def test_summary_create_template() -> None:
    """Test createTemplate endpoint with WireMock"""
    test_id = "summary.create_template.0"
    client = get_client(test_id)
    client.summary.create_template(
        name="name",
        example_summary="Patient John Doe, age 45, presents with hypertension diagnosed on 2024-01-15.",
        target_resources=["Patient", "Condition", "Observation"],
        mode="mode",
    )
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_get_template() -> None:
    """Test getTemplate endpoint with WireMock"""
    test_id = "summary.get_template.0"
    client = get_client(test_id)
    client.summary.get_template(
        id="id",
    )
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_update_template() -> None:
    """Test updateTemplate endpoint with WireMock"""
    test_id = "summary.update_template.0"
    client = get_client(test_id)
    client.summary.update_template(
        id="id",
        name="name",
        template="template",
        target_resources=["target_resources"],
        mode="mode",
    )
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_delete_template() -> None:
    """Test deleteTemplate endpoint with WireMock"""
    test_id = "summary.delete_template.0"
    client = get_client(test_id)
    client.summary.delete_template(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)


def test_summary_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "summary.create.0"
    client = get_client(test_id)
    client.summary.create(
        fhir_resources=FhirResource(
            resource_type="resourceType",
        ),
    )
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)
