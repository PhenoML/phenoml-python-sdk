from .conftest import get_client, verify_request_count


def test_tools_create_fhir_resource() -> None:
    """Test createFhirResource endpoint with WireMock"""
    test_id = "tools.create_fhir_resource.0"
    client = get_client(test_id)
    client.tools.create_fhir_resource(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        resource="auto",
        text="Patient John Doe has severe asthma with acute exacerbation",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resources_multi() -> None:
    """Test createFhirResourcesMulti endpoint with WireMock"""
    test_id = "tools.create_fhir_resources_multi.0"
    client = get_client(test_id)
    client.tools.create_fhir_resources_multi(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
        provider="medplum",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_search_fhir_resources() -> None:
    """Test searchFhirResources endpoint with WireMock"""
    test_id = "tools.search_fhir_resources.0"
    client = get_client(test_id)
    client.tools.search_fhir_resources(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        text="Find all appointments for patient John Doe next week",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-search", None, 1)


def test_tools_analyze_cohort() -> None:
    """Test analyzeCohort endpoint with WireMock"""
    test_id = "tools.analyze_cohort.0"
    client = get_client(test_id)
    client.tools.analyze_cohort(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        text="female patients over 20 with diabetes but not hypertension",
        provider="550e8400-e29b-41d4-a716-446655440000",
    )
    verify_request_count(test_id, "POST", "/tools/cohort", None, 1)
