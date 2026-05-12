from .conftest import get_client, verify_request_count


def test_lang2Fhir_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "lang2fhir.create.0"
    client = get_client(test_id)
    client.lang2fhir.create(
        version="R4",
        resource="condition-encounter-diagnosis",
        text="Patient has severe persistent asthma with acute exacerbation",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_multi() -> None:
    """Test createMulti endpoint with WireMock"""
    test_id = "lang2fhir.create_multi.0"
    client = get_client(test_id)
    client.lang2fhir.create_multi(
        text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily. Blood pressure 140/90.",
        version="R4",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_search() -> None:
    """Test search endpoint with WireMock"""
    test_id = "lang2fhir.search.0"
    client = get_client(test_id)
    client.lang2fhir.search(
        text="Appointments between March 2-9, 2025",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/search", None, 1)


def test_lang2Fhir_upload_profile() -> None:
    """Test uploadProfile endpoint with WireMock"""
    test_id = "lang2fhir.upload_profile.0"
    client = get_client(test_id)
    client.lang2fhir.upload_profile(
        profile="eyJyZXNvdXJjZVR5cGUiOiJTdHJ1Y3R1cmVEZWZpbml0aW9uIiwiaWQiOiJjdXN0b20tcGF0aWVudCIsInVybCI6Imh0dHA6Ly9waGVub21sLmNvbS9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vY3VzdG9tLXBhdGllbnQiLCJuYW1lIjoiQ3VzdG9tUGF0aWVudCIsInN0YXR1cyI6ImFjdGl2ZSIsImZoaXJWZXJzaW9uIjoiNC4wLjEiLCJraW5kIjoicmVzb3VyY2UiLCJhYnN0cmFjdCI6ZmFsc2UsInR5cGUiOiJQYXRpZW50IiwiYmFzZURlZmluaXRpb24iOiJodHRwOi8vaGw3Lm9yZy9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vUGF0aWVudCIsImRlcml2YXRpb24iOiJjb25zdHJhaW50Iiwic25hcHNob3QiOnsiZWxlbWVudCI6W3siaWQiOiJQYXRpZW50IiwicGF0aCI6IlBhdGllbnQiLCJtaW4iOjAsIm1heCI6IioifSx7ImlkIjoiUGF0aWVudC5uYW1lIiwicGF0aCI6IlBhdGllbnQubmFtZSIsIm1pbiI6MSwibWF4IjoiKiJ9XX19Cg==",
        implementation_guide="acme-cardiology",
        profile_context="When clinical text describes cardiology-specific findings, prefer this profile over the generic US Core Condition.",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_document() -> None:
    """Test document endpoint with WireMock"""
    test_id = "lang2fhir.document.0"
    client = get_client(test_id)
    client.lang2fhir.document(
        version="R4",
        resource="questionnaire",
        content="JVBERi0xLjQKJeLjz9MK...(base64-encoded PDF or image bytes)",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_extract_multiple_fhir_resources_from_a_document() -> None:
    """Test extractMultipleFhirResourcesFromADocument endpoint with WireMock"""
    test_id = "lang2fhir.extract_multiple_fhir_resources_from_a_document.0"
    client = get_client(test_id)
    client.lang2fhir.extract_multiple_fhir_resources_from_a_document(
        version="R4",
        content="JVBERi0xLjQKJeLjz9MK...(base64-encoded PDF or image bytes)",
        provider="medplum",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)
