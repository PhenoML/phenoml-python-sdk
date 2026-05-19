from .conftest import get_client, verify_request_count


def test_summary_summaryTemplates_list_templates() -> None:
    """Test listTemplates endpoint with WireMock"""
    test_id = "summary.summary_templates.list_templates.0"
    client = get_client(test_id)
    client.summary.summary_templates.list_templates()
    verify_request_count(test_id, "GET", "/fhir2summary/templates", None, 1)


def test_summary_summaryTemplates_create_template() -> None:
    """Test createTemplate endpoint with WireMock"""
    test_id = "summary.summary_templates.create_template.0"
    client = get_client(test_id)
    client.summary.summary_templates.create_template(
        name="Discharge Summary",
        example_summary="Patient John Doe, age 45, was admitted on 2024-01-10 with Type 2 Diabetes. Discharged on 2024-01-15 with Metformin 500mg BID.",
        target_resources=["Patient", "Condition", "MedicationRequest"],
        mode="narrative",
    )
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_summaryTemplates_get_template() -> None:
    """Test getTemplate endpoint with WireMock"""
    test_id = "summary.summary_templates.get_template.0"
    client = get_client(test_id)
    client.summary.summary_templates.get_template(
        id="id",
    )
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_summaryTemplates_update_template() -> None:
    """Test updateTemplate endpoint with WireMock"""
    test_id = "summary.summary_templates.update_template.0"
    client = get_client(test_id)
    client.summary.summary_templates.update_template(
        id="id",
        name="Discharge Summary",
        template="Patient {{Patient.name[0].text}} was discharged on {{Encounter[0].period.end}} with {{MedicationRequest[0].medicationCodeableConcept.coding[0].display}} {{MedicationRequest[0].dosageInstruction[0].text}}.",
        target_resources=["Patient", "Encounter", "MedicationRequest"],
        mode="narrative",
    )
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_summaryTemplates_delete_template() -> None:
    """Test deleteTemplate endpoint with WireMock"""
    test_id = "summary.summary_templates.delete_template.0"
    client = get_client(test_id)
    client.summary.summary_templates.delete_template(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)
