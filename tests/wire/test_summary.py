import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.summary import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError


def test_summary_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "summary.create.0"
    client = get_client(test_id)
    client.summary.create(
        mode="narrative",
        template_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        fhir_resources={
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "Patient",
                        "name": [{"given": ["John"], "family": "Doe"}],
                        "gender": "male",
                        "birthDate": "1979-03-15",
                    }
                },
                {
                    "resource": {
                        "resourceType": "Condition",
                        "code": {"text": "Type 2 Diabetes Mellitus"},
                        "onsetDateTime": "2024-01-15",
                    }
                },
            ],
        },
    )
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_international_patient_summary() -> None:
    """Test create endpoint (International Patient Summary example) with WireMock"""
    test_id = "summary.create.1"
    client = get_client(test_id)
    client.summary.create(
        mode="ips",
        fhir_resources={
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "Patient",
                        "id": "maria-garcia-001",
                        "name": [{"given": ["Maria"], "family": "Garcia"}],
                        "gender": "female",
                        "birthDate": "1985-07-22",
                    }
                },
                {
                    "resource": {
                        "resourceType": "AllergyIntolerance",
                        "code": {"text": "Penicillin"},
                        "criticality": "high",
                    }
                },
            ],
        },
    )
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "summary.create.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.summary.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "summary.create.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.summary.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_throws_forbidden_error() -> None:
    """Test create endpoint error response (ForbiddenError) with WireMock"""
    test_id = "summary.create.4"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.summary.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_throws_not_found_error() -> None:
    """Test create endpoint error response (NotFoundError) with WireMock"""
    test_id = "summary.create.5"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.summary.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)


def test_summary_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "summary.create.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.summary.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2summary/create", None, 1)
