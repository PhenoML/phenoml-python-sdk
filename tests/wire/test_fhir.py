from .conftest import get_client, verify_request_count

from phenoml.fhir import PatchRequestBodyItem


def test_fhir_search() -> None:
    """Test search endpoint with WireMock"""
    test_id = "fhir.search.0"
    client = get_client(test_id)
    client.fhir.search(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    )
    verify_request_count(test_id, "GET", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "fhir.create.0"
    client = get_client(test_id)
    client.fhir.create(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        request={"resourceType": "Patient"},
    )
    verify_request_count(test_id, "POST", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_upsert() -> None:
    """Test upsert endpoint with WireMock"""
    test_id = "fhir.upsert.0"
    client = get_client(test_id)
    client.fhir.upsert(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        request={"resourceType": "Patient", "id": "123"},
    )
    verify_request_count(test_id, "PUT", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fhir.delete.0"
    client = get_client(test_id)
    client.fhir.delete(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    )
    verify_request_count(test_id, "DELETE", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "fhir.patch.0"
    client = get_client(test_id)
    client.fhir.patch(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        request=[
            PatchRequestBodyItem(
                op="replace",
                path="/name/0/family",
                value="NewFamilyName",
            )
        ],
    )
    verify_request_count(test_id, "PATCH", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_execute_bundle() -> None:
    """Test executeBundle endpoint with WireMock"""
    test_id = "fhir.execute_bundle.0"
    client = get_client(test_id)
    client.fhir.execute_bundle(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        request={
            "resourceType": "Bundle",
            "type": "transaction",
            "entry": [
                {
                    "request": {"method": "POST", "url": "Patient"},
                    "resource": {"resourceType": "Patient", "name": [{"family": "Doe", "given": ["John"]}]},
                },
                {
                    "request": {"method": "POST", "url": "Observation"},
                    "resource": {
                        "resourceType": "Observation",
                        "status": "final",
                        "subject": {"reference": "Patient/123"},
                    },
                },
            ],
        },
    )
    verify_request_count(test_id, "POST", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir", None, 1)
