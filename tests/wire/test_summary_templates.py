import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.summary import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError


def test_summary_templates_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "summary.templates.list_.0"
    client = get_client(test_id)
    client.summary.templates.list()
    verify_request_count(test_id, "GET", "/fhir2summary/templates", None, 1)


def test_summary_templates_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.templates.list_.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.templates.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir2summary/templates", None, 1)


def test_summary_templates_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.templates.list_.2"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.templates.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_summary_templates_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "summary.templates.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.summary.templates.create(
            name="name",
            example_summary="example_summary",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_templates_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.templates.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.templates.create(
            name="name",
            example_summary="example_summary",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_templates_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.templates.create.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.templates.create(
            name="name",
            example_summary="example_summary",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/template", None, 1)


def test_summary_templates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "summary.templates.get.0"
    client = get_client(test_id)
    client.summary.templates.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_templates_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.templates.get.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.templates.get(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_templates_get_throws_forbidden_error() -> None:
    """Test get endpoint error response (ForbiddenError) with WireMock"""
    test_id = "summary.templates.get.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.summary.templates.get(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_templates_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "summary.templates.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.summary.templates.get(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/fhir2summary/template/id", None, 1)


def test_summary_templates_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.templates.get.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.templates.get(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_summary_templates_update_throws_bad_request_error() -> None:
    """Test update endpoint error response (BadRequestError) with WireMock"""
    test_id = "summary.templates.update.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.summary.templates.update(
            id="id",
            name="name",
            template="template",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_update_throws_unauthorized_error() -> None:
    """Test update endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.templates.update.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.templates.update(
            id="id",
            name="name",
            template="template",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_update_throws_forbidden_error() -> None:
    """Test update endpoint error response (ForbiddenError) with WireMock"""
    test_id = "summary.templates.update.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.summary.templates.update(
            id="id",
            name="name",
            template="template",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_update_throws_not_found_error() -> None:
    """Test update endpoint error response (NotFoundError) with WireMock"""
    test_id = "summary.templates.update.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.summary.templates.update(
            id="id",
            name="name",
            template="template",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_update_throws_internal_server_error() -> None:
    """Test update endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.templates.update.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.templates.update(
            id="id",
            name="name",
            template="template",
            target_resources=["target_resources", "target_resources"],
            mode="mode",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "PUT", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "summary.templates.delete.0"
    client = get_client(test_id)
    client.summary.templates.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete_throws_unauthorized_error() -> None:
    """Test delete endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.templates.delete.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.templates.delete(
            id="id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete_throws_forbidden_error() -> None:
    """Test delete endpoint error response (ForbiddenError) with WireMock"""
    test_id = "summary.templates.delete.2"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.summary.templates.delete(
            id="id",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete_throws_not_found_error() -> None:
    """Test delete endpoint error response (NotFoundError) with WireMock"""
    test_id = "summary.templates.delete.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.summary.templates.delete(
            id="id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)


def test_summary_templates_delete_throws_internal_server_error() -> None:
    """Test delete endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.templates.delete.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.templates.delete(
            id="id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "DELETE", "/fhir2summary/template/id", None, 1)
