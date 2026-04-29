from .conftest import get_client, verify_request_count


def test_lang2Fhir_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "lang2fhir.create.0"
    client = get_client(test_id)
    client.lang2fhir.create(
        version="R4",
        resource="auto",
        text="Patient has severe asthma with acute exacerbation",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_multi() -> None:
    """Test createMulti endpoint with WireMock"""
    test_id = "lang2fhir.create_multi.0"
    client = get_client(test_id)
    client.lang2fhir.create_multi(
        text="John Smith, male born on 1980-03-12, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
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
        profile="(base64 encoded FHIR StructureDefinition JSON)",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_document() -> None:
    """Test document endpoint with WireMock"""
    test_id = "lang2fhir.document.0"
    client = get_client(test_id)
    client.lang2fhir.document(
        version="R4",
        resource="questionnaire",
        content="content",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_extract_multiple_fhir_resources_from_a_document() -> None:
    """Test extractMultipleFhirResourcesFromADocument endpoint with WireMock"""
    test_id = "lang2fhir.extract_multiple_fhir_resources_from_a_document.0"
    client = get_client(test_id)
    client.lang2fhir.extract_multiple_fhir_resources_from_a_document(
        version="R4",
        content="content",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)
