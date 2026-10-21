import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.lang2fhir import (
    BadRequestError,
    ClientClosedRequestError,
    DocumentConfig,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    SplitClassification,
    UnauthorizedError,
    UnprocessableEntityError,
)


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


def test_lang2Fhir_create_medication_request() -> None:
    """Test create endpoint (MedicationRequest example) with WireMock"""
    test_id = "lang2fhir.create.1"
    client = get_client(test_id)
    client.lang2fhir.create(
        version="R4",
        resource="medicationrequest",
        text="Prescribe Amoxicillin 500mg capsules, take one capsule three times daily for 10 days",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.create.2"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.create(
            version="R4",
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.create.3"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.create(
            version="R4",
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_throws_not_found_error() -> None:
    """Test create endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir.create.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir.create(
            version="R4",
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_throws_unprocessable_entity_error() -> None:
    """Test create endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "lang2fhir.create.5"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.lang2fhir.create(
            version="R4",
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create", None, 1)


def test_lang2Fhir_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.create.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.create(
            version="R4",
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_lang2Fhir_create_multi_throws_bad_request_error() -> None:
    """Test createMulti endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.create_multi.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.create_multi(
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_create_multi_throws_unauthorized_error() -> None:
    """Test createMulti endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.create_multi.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.create_multi(
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_create_multi_throws_not_found_error() -> None:
    """Test createMulti endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir.create_multi.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir.create_multi(
            text="text",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_create_multi_throws_unprocessable_entity_error() -> None:
    """Test createMulti endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "lang2fhir.create_multi.4"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.lang2fhir.create_multi(
            text="text",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_create_multi_throws_internal_server_error() -> None:
    """Test createMulti endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.create_multi.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.create_multi(
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/create/multi", None, 1)


def test_lang2Fhir_search() -> None:
    """Test search endpoint with WireMock"""
    test_id = "lang2fhir.search.0"
    client = get_client(test_id)
    client.lang2fhir.search(
        text="Appointments between March 2-9, 2025",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/search", None, 1)


def test_lang2Fhir_search_throws_bad_request_error() -> None:
    """Test search endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.search.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.search(
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/search", None, 1)


def test_lang2Fhir_search_throws_unauthorized_error() -> None:
    """Test search endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.search.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.search(
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/search", None, 1)


def test_lang2Fhir_search_throws_internal_server_error() -> None:
    """Test search endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.search.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.search(
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_lang2Fhir_upload_profile_throws_bad_request_error() -> None:
    """Test uploadProfile endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.upload_profile.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.upload_profile(
            profile="profile",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_upload_profile_throws_unauthorized_error() -> None:
    """Test uploadProfile endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.upload_profile.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.upload_profile(
            profile="profile",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_upload_profile_throws_forbidden_error() -> None:
    """Test uploadProfile endpoint error response (ForbiddenError) with WireMock"""
    test_id = "lang2fhir.upload_profile.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.lang2fhir.upload_profile(
            profile="profile",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_upload_profile_throws_internal_server_error() -> None:
    """Test uploadProfile endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.upload_profile.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.upload_profile(
            profile="profile",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/profile/upload", None, 1)


def test_lang2Fhir_document() -> None:
    """Test document endpoint with WireMock"""
    test_id = "lang2fhir.document.0"
    client = get_client(test_id)
    client.lang2fhir.document(
        version="R4",
        resource="questionnaire",
        content="JVBERi0xLjQKJeLjz9MK...(base64-encoded document bytes)",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_bad_request_error() -> None:
    """Test document endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.document.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_unauthorized_error() -> None:
    """Test document endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.document.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_forbidden_error() -> None:
    """Test document endpoint error response (ForbiddenError) with WireMock"""
    test_id = "lang2fhir.document.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_not_found_error() -> None:
    """Test document endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir.document.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_unprocessable_entity_error() -> None:
    """Test document endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "lang2fhir.document.5"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_client_closed_request_error() -> None:
    """Test document endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir.document.6"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_internal_server_error() -> None:
    """Test document endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.document.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_throws_gateway_timeout_error() -> None:
    """Test document endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir.document.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir.document(
            version="version",
            resource="resource",
            content="content",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document", None, 1)


def test_lang2Fhir_document_multi() -> None:
    """Test documentMulti endpoint with WireMock"""
    test_id = "lang2fhir.document_multi.0"
    client = get_client(test_id)
    client.lang2fhir.document_multi(
        version="R4",
        content="JVBERi0xLjQKJeLjz9MK...(base64-encoded document bytes)",
        provider="medplum",
        config=DocumentConfig(
            split_classifications=[
                SplitClassification(
                    id="clinical",
                    description="Clinical notes, diagnoses, medications, observations, and patient demographics.",
                    operation="group",
                ),
                SplitClassification(
                    id="admin",
                    description="Administrative boilerplate, insurance forms, and cover sheets.",
                    operation="drop",
                ),
            ],
        ),
    )
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_bad_request_error() -> None:
    """Test documentMulti endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir.document_multi.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_unauthorized_error() -> None:
    """Test documentMulti endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir.document_multi.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_forbidden_error() -> None:
    """Test documentMulti endpoint error response (ForbiddenError) with WireMock"""
    test_id = "lang2fhir.document_multi.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_not_found_error() -> None:
    """Test documentMulti endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir.document_multi.4"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_unprocessable_entity_error() -> None:
    """Test documentMulti endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "lang2fhir.document_multi.5"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_client_closed_request_error() -> None:
    """Test documentMulti endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir.document_multi.6"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_internal_server_error() -> None:
    """Test documentMulti endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir.document_multi.7"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)


def test_lang2Fhir_document_multi_throws_gateway_timeout_error() -> None:
    """Test documentMulti endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir.document_multi.8"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir.document_multi(
            version="version",
            content="content",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/document/multi", None, 1)
