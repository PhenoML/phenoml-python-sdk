from .conftest import get_client, verify_request_count

from phenoml.construe import CodeResponse, ExtractCodesResult, ExtractedCodeResult, ExtractRequestSystem


def test_construe_upload_code_system() -> None:
    """Test uploadCodeSystem endpoint with WireMock"""
    test_id = "construe.upload_code_system.0"
    client = get_client(test_id)
    client.construe.upload_code_system(
        name="CUSTOM_CODES",
        version="1.0",
        format="json",
        codes=[
            CodeResponse(
                code="X001",
                description="Example custom code 1",
            ),
            CodeResponse(
                code="X002",
                description="Example custom code 2",
            ),
        ],
    )
    verify_request_count(test_id, "POST", "/construe/upload", None, 1)


def test_construe_extract_codes() -> None:
    """Test extractCodes endpoint with WireMock"""
    test_id = "construe.extract_codes.0"
    client = get_client(test_id)
    client.construe.extract_codes(
        text="Patient is a 14-year-old female, previously healthy, who is here for evaluation of abnormal renal ultrasound with atrophic right kidney.",
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="2025",
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_list_available_code_systems() -> None:
    """Test listAvailableCodeSystems endpoint with WireMock"""
    test_id = "construe.list_available_code_systems.0"
    client = get_client(test_id)
    client.construe.list_available_code_systems()
    verify_request_count(test_id, "GET", "/construe/codes/systems", None, 1)


def test_construe_get_code_system_detail() -> None:
    """Test getCodeSystemDetail endpoint with WireMock"""
    test_id = "construe.get_code_system_detail.0"
    client = get_client(test_id)
    client.construe.get_code_system_detail(
        codesystem="ICD-10-CM",
        version="2025",
    )
    verify_request_count(test_id, "GET", "/construe/codes/systems/ICD-10-CM", {"version": "2025"}, 1)


def test_construe_delete_custom_code_system() -> None:
    """Test deleteCustomCodeSystem endpoint with WireMock"""
    test_id = "construe.delete_custom_code_system.0"
    client = get_client(test_id)
    client.construe.delete_custom_code_system(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "DELETE", "/construe/codes/systems/CUSTOM_CODES", {"version": "version"}, 1)


def test_construe_export_custom_code_system() -> None:
    """Test exportCustomCodeSystem endpoint with WireMock"""
    test_id = "construe.export_custom_code_system.0"
    client = get_client(test_id)
    client.construe.export_custom_code_system(
        codesystem="CUSTOM_CODES",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/systems/CUSTOM_CODES/export", {"version": "version"}, 1)


def test_construe_list_codes_in_a_code_system() -> None:
    """Test listCodesInACodeSystem endpoint with WireMock"""
    test_id = "construe.list_codes_in_a_code_system.0"
    client = get_client(test_id)
    client.construe.list_codes_in_a_code_system(
        codesystem="ICD-10-CM",
        version="2025",
        cursor="cursor",
        limit=1,
    )
    verify_request_count(
        test_id, "GET", "/construe/codes/ICD-10-CM", {"version": "2025", "cursor": "cursor", "limit": "1"}, 1
    )


def test_construe_get_a_specific_code() -> None:
    """Test getASpecificCode endpoint with WireMock"""
    test_id = "construe.get_a_specific_code.0"
    client = get_client(test_id)
    client.construe.get_a_specific_code(
        codesystem="ICD-10-CM",
        code_id="E1165",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/ICD-10-CM/E1165", {"version": "version"}, 1)


def test_construe_semantic_search_embedding_based() -> None:
    """Test semanticSearchEmbeddingBased endpoint with WireMock"""
    test_id = "construe.semantic_search_embedding_based.0"
    client = get_client(test_id)
    client.construe.semantic_search_embedding_based(
        codesystem="ICD-10-CM",
        text="patient has trouble breathing at night and wakes up gasping",
        version="version",
        limit=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/construe/codes/ICD-10-CM/search/semantic",
        {"text": "patient has trouble breathing at night and wakes up gasping", "version": "version", "limit": "1"},
        1,
    )


def test_construe_submit_feedback_on_extraction_results() -> None:
    """Test submitFeedbackOnExtractionResults endpoint with WireMock"""
    test_id = "construe.submit_feedback_on_extraction_results.0"
    client = get_client(test_id)
    client.construe.submit_feedback_on_extraction_results(
        text="Patient has type 2 diabetes with hyperglycemia",
        received_result=ExtractCodesResult(
            system=ExtractRequestSystem(
                name="ICD-10-CM",
                version="2025",
            ),
            codes=[
                ExtractedCodeResult(
                    code="E11.9",
                    description="Type 2 diabetes mellitus without complications",
                    valid=True,
                )
            ],
        ),
        expected_result=ExtractCodesResult(
            system=ExtractRequestSystem(
                name="ICD-10-CM",
                version="2025",
            ),
            codes=[
                ExtractedCodeResult(
                    code="E11.65",
                    description="Type 2 diabetes mellitus with hyperglycemia",
                    valid=True,
                )
            ],
        ),
        detail="Expected code E11.65 because the text mentions hyperglycemia",
    )
    verify_request_count(test_id, "POST", "/construe/feedback", None, 1)


def test_construe_terminology_server_text_search() -> None:
    """Test terminologyServerTextSearch endpoint with WireMock"""
    test_id = "construe.terminology_server_text_search.0"
    client = get_client(test_id)
    client.construe.terminology_server_text_search(
        codesystem="ICD-10-CM",
        q="E11.65",
        version="version",
        limit=1,
    )
    verify_request_count(
        test_id, "GET", "/construe/codes/ICD-10-CM/search/text", {"q": "E11.65", "version": "version", "limit": "1"}, 1
    )
