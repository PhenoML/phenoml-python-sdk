from .conftest import get_client, verify_request_count


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
