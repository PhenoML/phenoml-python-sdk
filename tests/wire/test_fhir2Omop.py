import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.fhir2omop import BadRequestError, InternalServerError, UnauthorizedError


def test_fhir2Omop_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "fhir2omop.create.0"
    client = get_client(test_id)
    client.fhir2omop.create(
        fhir_resources={
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "Patient",
                        "id": "patient-1",
                        "gender": "female",
                        "birthDate": "1985-07-22",
                    }
                },
                {
                    "resource": {
                        "resourceType": "Condition",
                        "id": "condition-1",
                        "subject": {"reference": "Patient/patient-1"},
                        "code": {
                            "coding": [
                                {
                                    "system": "http://snomed.info/sct",
                                    "code": "44054006",
                                    "display": "Type 2 diabetes mellitus",
                                }
                            ]
                        },
                        "onsetDateTime": "2024-01-15",
                    }
                },
                {
                    "resource": {
                        "resourceType": "MedicationRequest",
                        "id": "medreq-1",
                        "status": "active",
                        "intent": "order",
                        "subject": {"reference": "Patient/patient-1"},
                        "medicationReference": {"reference": "#med0"},
                        "authoredOn": "2024-01-16",
                        "contained": [
                            {
                                "resourceType": "Medication",
                                "id": "med0",
                                "code": {
                                    "coding": [
                                        {
                                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                                            "code": "860975",
                                            "display": "metformin hydrochloride 500 MG",
                                        }
                                    ]
                                },
                            }
                        ],
                    }
                },
            ],
        },
    )
    verify_request_count(test_id, "POST", "/fhir2omop/create", None, 1)


def test_fhir2Omop_create_oid_form_loinc_coding() -> None:
    """Test create endpoint (OID-form LOINC coding example) with WireMock"""
    test_id = "fhir2omop.create.1"
    client = get_client(test_id)
    client.fhir2omop.create(
        fhir_resources={
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {"resource": {"resourceType": "Patient", "id": "patient-1"}},
                {
                    "resource": {
                        "resourceType": "Observation",
                        "id": "hemoglobin-1",
                        "status": "final",
                        "subject": {"reference": "Patient/patient-1"},
                        "code": {
                            "coding": [
                                {"system": "urn:oid:2.16.840.1.113883.6.1", "code": "718-7", "display": "Hemoglobin"}
                            ]
                        },
                        "valueQuantity": {"value": 13.5, "unit": "g/dL"},
                    }
                },
            ],
        },
    )
    verify_request_count(test_id, "POST", "/fhir2omop/create", None, 1)


def test_fhir2Omop_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "fhir2omop.create.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.fhir2omop.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2omop/create", None, 1)


def test_fhir2Omop_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "fhir2omop.create.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.fhir2omop.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2omop/create", None, 1)


def test_fhir2Omop_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "fhir2omop.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.fhir2omop.create(
            fhir_resources={"fhir_resources": {"key": "value"}},
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/fhir2omop/create", None, 1)
