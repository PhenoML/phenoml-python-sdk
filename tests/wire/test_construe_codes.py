import pytest
from .conftest import get_client, verify_request_count

from phenoml.construe import (
    BadRequestError,
    ExtractRequestConfig,
    ExtractRequestSystem,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    NotImplementedError,
    PhenocrExtractRequestSystem,
    ServiceUnavailableError,
    UnauthorizedError,
)
from phenoml.core.jsonable_encoder import jsonable_encoder


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


def test_construe_codes_extract_icd10cm_umls_2026aa() -> None:
    """Test extract endpoint (ICD-10-CM UMLS 2026AA example) with WireMock"""
    test_id = "construe.codes.extract.1"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="Patient has type 2 diabetes mellitus with diabetic chronic kidney disease.",
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="umls-2026aa",
        ),
        config=ExtractRequestConfig(
            validation_method="simple",
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_with_source_citations() -> None:
    """Test extract endpoint (With Source Citations example) with WireMock"""
    test_id = "construe.codes.extract.2"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="45-year-old male presents with chest pain radiating to left arm, shortness of breath, and diaphoresis. ECG shows ST elevation in leads II, III, and aVF.",
        system=ExtractRequestSystem(
            name="SNOMED_CT_US_LITE",
            version="20240901",
        ),
        config=ExtractRequestConfig(
            chunking_method="sentences",
            validation_method="simple",
            include_rationale=True,
            include_citations=True,
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_medication_validation() -> None:
    """Test extract endpoint (Medication Validation example) with WireMock"""
    test_id = "construe.codes.extract.3"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="Start Metformin 500mg twice daily for type 2 diabetes. Continue Lisinopril 10mg daily for hypertension. Add Atorvastatin 20mg at bedtime.",
        system=ExtractRequestSystem(
            name="RXNORM",
            version="11042024",
        ),
        config=ExtractRequestConfig(
            validation_method="medication_search",
            include_rationale=True,
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_with_ancestor_codes() -> None:
    """Test extract endpoint (With Ancestor Codes example) with WireMock"""
    test_id = "construe.codes.extract.4"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="Patient diagnosed with Type 2 diabetes mellitus with diabetic chronic kidney disease, stage 3.",
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="2025",
        ),
        config=ExtractRequestConfig(
            validation_method="simple",
            include_ancestors=True,
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_hpo_phenotype_extraction() -> None:
    """Test extract endpoint (HPO Phenotype Extraction example) with WireMock"""
    test_id = "construe.codes.extract.5"
    client = get_client(test_id)
    client.construe.codes.extract(
        text="5-year-old male with seizures, severe intellectual disability, microcephaly, and hypotonia.",
        system=ExtractRequestSystem(
            name="HPO",
            version="2025",
        ),
        config=ExtractRequestConfig(
            chunking_method="fasthpocr",
            validation_method="none",
            include_rationale=False,
        ),
    )
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_bad_request_error() -> None:
    """Test extract endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.extract.6"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_unauthorized_error() -> None:
    """Test extract endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.extract.7"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_not_found_error() -> None:
    """Test extract endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.extract.8"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_internal_server_error() -> None:
    """Test extract endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.extract.9"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_service_unavailable_error() -> None:
    """Test extract endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "construe.codes.extract.10"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/extract", None, 1)


def test_construe_codes_extract_throws_gateway_timeout_error() -> None:
    """Test extract endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "construe.codes.extract.11"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.construe.codes.extract(
            text="text",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_construe_codes_phenocr_throws_bad_request_error() -> None:
    """Test phenocr endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.phenocr.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_phenocr_throws_unauthorized_error() -> None:
    """Test phenocr endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.phenocr.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_phenocr_throws_not_found_error() -> None:
    """Test phenocr endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.phenocr.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_phenocr_throws_internal_server_error() -> None:
    """Test phenocr endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.phenocr.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_phenocr_throws_service_unavailable_error() -> None:
    """Test phenocr endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "construe.codes.phenocr.5"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_phenocr_throws_gateway_timeout_error() -> None:
    """Test phenocr endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "construe.codes.phenocr.6"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.construe.codes.phenocr(
            text="text",
            system=PhenocrExtractRequestSystem(
                name="name",
                version="version",
            ),
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/phenocr", None, 1)


def test_construe_codes_crosswalk() -> None:
    """Test crosswalk endpoint with WireMock"""
    test_id = "construe.codes.crosswalk.0"
    client = get_client(test_id)
    client.construe.codes.crosswalk(
        system="http://hl7.org/fhir/sid/icd-10-cm",
        code="A02.24",
        targets=["http://human-phenotype-ontology.org"],
    )
    verify_request_count(test_id, "POST", "/construe/codes/crosswalk", None, 1)


def test_construe_codes_crosswalk_throws_bad_request_error() -> None:
    """Test crosswalk endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.crosswalk.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.crosswalk(
            system="system",
            code="code",
            targets=["targets", "targets"],
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/codes/crosswalk", None, 1)


def test_construe_codes_crosswalk_throws_unauthorized_error() -> None:
    """Test crosswalk endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.crosswalk.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.crosswalk(
            system="system",
            code="code",
            targets=["targets", "targets"],
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/codes/crosswalk", None, 1)


def test_construe_codes_crosswalk_throws_internal_server_error() -> None:
    """Test crosswalk endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.crosswalk.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.crosswalk(
            system="system",
            code="code",
            targets=["targets", "targets"],
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/codes/crosswalk", None, 1)


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


def test_construe_codes_list__browse_snomed() -> None:
    """Test list endpoint (Browse SNOMED example) with WireMock"""
    test_id = "construe.codes.list_.1"
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


def test_construe_codes_list__throws_bad_request_error() -> None:
    """Test list endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.list_.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.list(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem", None, 1)


def test_construe_codes_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.list_.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.list(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem", None, 1)


def test_construe_codes_list__throws_not_found_error() -> None:
    """Test list endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.list_.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.list(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem", None, 1)


def test_construe_codes_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.list_.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.list(
            codesystem="codesystem",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem", None, 1)


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


def test_construe_codes_lookup_look_up_snomed_concept() -> None:
    """Test lookup endpoint (Look Up SNOMED Concept example) with WireMock"""
    test_id = "construe.codes.lookup.1"
    client = get_client(test_id)
    client.construe.codes.lookup(
        codesystem="ICD-10-CM",
        code_id="E1165",
        version="version",
    )
    verify_request_count(test_id, "GET", "/construe/codes/ICD-10-CM/E1165", {"version": "version"}, 1)


def test_construe_codes_lookup_throws_bad_request_error() -> None:
    """Test lookup endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.lookup.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.lookup(
            codesystem="codesystem",
            code_id="codeID",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/codeID", None, 1)


def test_construe_codes_lookup_throws_unauthorized_error() -> None:
    """Test lookup endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.lookup.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.lookup(
            codesystem="codesystem",
            code_id="codeID",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/codeID", None, 1)


def test_construe_codes_lookup_throws_not_found_error() -> None:
    """Test lookup endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.lookup.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.lookup(
            codesystem="codesystem",
            code_id="codeID",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/codeID", None, 1)


def test_construe_codes_lookup_throws_internal_server_error() -> None:
    """Test lookup endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.lookup.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.lookup(
            codesystem="codesystem",
            code_id="codeID",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/codeID", None, 1)


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


def test_construe_codes_search_semantic_diabetes_complications() -> None:
    """Test searchSemantic endpoint (Diabetes Complications example) with WireMock"""
    test_id = "construe.codes.search_semantic.1"
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


def test_construe_codes_search_semantic_throws_bad_request_error() -> None:
    """Test searchSemantic endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.search_semantic.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.search_semantic(
            codesystem="codesystem",
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/semantic", {"text": "text"}, 1)


def test_construe_codes_search_semantic_throws_unauthorized_error() -> None:
    """Test searchSemantic endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.search_semantic.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.search_semantic(
            codesystem="codesystem",
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/semantic", {"text": "text"}, 1)


def test_construe_codes_search_semantic_throws_not_found_error() -> None:
    """Test searchSemantic endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.search_semantic.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.search_semantic(
            codesystem="codesystem",
            text="text",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/semantic", {"text": "text"}, 1)


def test_construe_codes_search_semantic_throws_internal_server_error() -> None:
    """Test searchSemantic endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.search_semantic.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.search_semantic(
            codesystem="codesystem",
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/semantic", {"text": "text"}, 1)


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


def test_construe_codes_search_text_search_by_description() -> None:
    """Test searchText endpoint (Search by Description example) with WireMock"""
    test_id = "construe.codes.search_text.1"
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


def test_construe_codes_search_text_throws_bad_request_error() -> None:
    """Test searchText endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.codes.search_text.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.codes.search_text(
            codesystem="codesystem",
            q="q",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/text", {"q": "q"}, 1)


def test_construe_codes_search_text_throws_unauthorized_error() -> None:
    """Test searchText endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.codes.search_text.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.codes.search_text(
            codesystem="codesystem",
            q="q",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/text", {"q": "q"}, 1)


def test_construe_codes_search_text_throws_not_found_error() -> None:
    """Test searchText endpoint error response (NotFoundError) with WireMock"""
    test_id = "construe.codes.search_text.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.construe.codes.search_text(
            codesystem="codesystem",
            q="q",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/text", {"q": "q"}, 1)


def test_construe_codes_search_text_throws_internal_server_error() -> None:
    """Test searchText endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.codes.search_text.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.codes.search_text(
            codesystem="codesystem",
            q="q",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/text", {"q": "q"}, 1)


def test_construe_codes_search_text_throws_not_implemented_error() -> None:
    """Test searchText endpoint error response (NotImplementedError) with WireMock"""
    test_id = "construe.codes.search_text.6"
    client = get_client(test_id)
    with pytest.raises(NotImplementedError) as exc_info:
        client.construe.codes.search_text(
            codesystem="codesystem",
            q="q",
        )
    assert exc_info.value.status_code == 501
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/construe/codes/codesystem/search/text", {"q": "q"}, 1)
