from .conftest import get_client, verify_request_count


def test_summary_templates_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "summary.templates.list_.0"
    client = get_client(test_id)
    client.summary.templates.list()
    verify_request_count(test_id, "GET", "/fhir2summary/templates", None, 1)


def test_summary_templates_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "summary.templates.create.0"
    client = get_client(test_id)
    client.summary.templates.create(
        name="Discharge Summary",
        example_summary="Patient John Doe, age 45, was admitted on 2024-01-10 with Type 2 Diabetes. Discharged on 2024-01-15 with Metformin 500mg BID.",
        target_resources=["Patient", "Condition", "MedicationRequest"],
        mode="narrative",
    )
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_templates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "summary.templates.get.0"
    client = get_client(test_id)
    client.summary.templates.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_templates_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "summary.templates.update.0"
    client = get_client(test_id)
    client.summary.templates.update(
        id="id",
        name="Discharge Summary",
        template="Patient {{Patient.name[0].text}} was discharged on {{Encounter[0].period.end}} with {{MedicationRequest[0].medicationCodeableConcept.coding[0].display}} {{MedicationRequest[0].dosageInstruction[0].text}}.",
        target_resources=["Patient", "Encounter", "MedicationRequest"],
        mode="narrative",
    )
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "summary.templates.delete.0"
    client = get_client(test_id)
    client.summary.templates.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)
