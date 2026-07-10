from .conftest import get_client, verify_request_count

from phenoml.construe import ExtractRequestSystem, PhenocrExtractRequestSystem


def test_construe_codes_extract() -> None:
    """Test extract endpoint with WireMock"""
    test_id = "construe.codes.extract.0"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="Patient is a 14-year-old female, previously healthy, who is here for evaluation of abnormal renal ultrasound with atrophic right kidney.",
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="2025",
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_phenocr() -> None:
    """Test phenocr endpoint with WireMock"""
    test_id = "construe.codes.phenocr.0"
    client = get_client(test_id)
    client.construe.codes.phenocr(
        text="5-year-old male with seizures, severe intellectual disability, microcephaly, and hypotonia.",
        system=PhenocrExtractRequestSystem(
            name="HPO",
            version="umls-2026AA",
        ),
    )
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "construe.codes.list_.0"
    client = get_client(test_id)
    client.construe.codes.list(
        codesystem="ICD-10-CM",
        version="2025",
        cursor="cursor",
        limit=1,
    )
    verify_request_count(
        test_id, "GET", "/construe/codes/ICD-10-CM", {"version": "2025", "cursor": "cursor", "limit": "1"}, 1
    )


def test_construe_codes_lookup() -> None:
    """Test lookup endpoint with WireMock"""
    test_id = "construe.codes.lookup.0"
    client = get_client(test_id)
    client.construe.codes.lookup(
        codesystem="ICD-10-CM",
        code_id="E1165",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/ICD-10-CM/E1165", {"version": "version"}, 1)


def test_construe_codes_search_semantic() -> None:
    """Test searchSemantic endpoint with WireMock"""
    test_id = "construe.codes.search_semantic.0"
    client = get_client(test_id)
    client.construe.codes.search_semantic(
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


def test_construe_codes_search_text() -> None:
    """Test searchText endpoint with WireMock"""
    test_id = "construe.codes.search_text.0"
    client = get_client(test_id)
    client.construe.codes.search_text(
        codesystem="ICD-10-CM",
        q="E11.65",
        version="version",
        limit=1,
    )
    verify_request_count(
        test_id, "GET", "/construe/codes/ICD-10-CM/search/text", {"q": "E11.65", "version": "version", "limit": "1"}, 1
    )
