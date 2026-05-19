from .conftest import get_client, verify_request_count


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
