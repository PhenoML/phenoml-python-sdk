from .conftest import get_client, verify_request_count

from phenoml.fhir import FhirBundleEntryItem, FhirBundleEntryItemRequest
from phenoml.fhir.fhir_operations import PatchRequestBodyItem


def test_fhir_fhirOperations_search() -> None:
    """Test search endpoint with WireMock"""
    test_id = "fhir.fhir_operations.search.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.search(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    )
    verify_request_count(test_id, "GET", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_fhirOperations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "fhir.fhir_operations.create.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.create(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        resource_type="Patient",
    )
    verify_request_count(test_id, "POST", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_fhirOperations_upsert() -> None:
    """Test upsert endpoint with WireMock"""
    test_id = "fhir.fhir_operations.upsert.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.upsert(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        resource_type="Patient",
        id="123",
    )
    verify_request_count(test_id, "PUT", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_fhirOperations_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fhir.fhir_operations.delete.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.delete(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        fhir_path="Patient",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    )
    verify_request_count(test_id, "DELETE", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir/Patient", None, 1)


def test_fhir_fhirOperations_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "fhir.fhir_operations.patch.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.patch(
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


def test_fhir_fhirOperations_execute_bundle() -> None:
    """Test executeBundle endpoint with WireMock"""
    test_id = "fhir.fhir_operations.execute_bundle.0"
    client = get_client(test_id)
    client.fhir.fhir_operations.execute_bundle(
        fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        entry=[
            FhirBundleEntryItem(
                resource={"resourceType": "Patient", "name": [{"family": "Doe", "given": ["John"]}]},
                request=FhirBundleEntryItemRequest(
                    method="POST",
                    url="Patient",
                ),
            ),
            FhirBundleEntryItem(
                resource={"resourceType": "Observation", "status": "final", "subject": {"reference": "Patient/123"}},
                request=FhirBundleEntryItemRequest(
                    method="POST",
                    url="Observation",
                ),
            ),
        ],
    )
    verify_request_count(test_id, "POST", "/fhir-provider/550e8400-e29b-41d4-a716-446655440000/fhir", None, 1)
