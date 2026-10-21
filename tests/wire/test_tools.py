import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.tools import BadRequestError, ForbiddenError, InternalServerError, UnauthorizedError


def test_tools_create_fhir_resource() -> None:
    """Test createFhirResource endpoint with WireMock"""
    test_id = "tools.create_fhir_resource.0"
    client = get_client(test_id)
    client.tools.create_fhir_resource(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        resource="condition-encounter-diagnosis",
        text="Patient has severe persistent asthma with acute exacerbation",
        provider="550e8400-e29b-41d4-a716-446655440000",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resource_throws_bad_request_error() -> None:
    """Test createFhirResource endpoint error response (BadRequestError) with WireMock"""
    test_id = "tools.create_fhir_resource.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tools.create_fhir_resource(
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resource_throws_unauthorized_error() -> None:
    """Test createFhirResource endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.create_fhir_resource.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.create_fhir_resource(
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resource_throws_forbidden_error() -> None:
    """Test createFhirResource endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.create_fhir_resource.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.create_fhir_resource(
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resource_throws_internal_server_error() -> None:
    """Test createFhirResource endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.create_fhir_resource.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.create_fhir_resource(
            resource="auto",
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create", None, 1)


def test_tools_create_fhir_resources_multi() -> None:
    """Test createFhirResourcesMulti endpoint with WireMock"""
    test_id = "tools.create_fhir_resources_multi.0"
    client = get_client(test_id)
    client.tools.create_fhir_resources_multi(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
        version="R4",
        provider="medplum",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_create_fhir_resources_multi_throws_bad_request_error() -> None:
    """Test createFhirResourcesMulti endpoint error response (BadRequestError) with WireMock"""
    test_id = "tools.create_fhir_resources_multi.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tools.create_fhir_resources_multi(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_create_fhir_resources_multi_throws_unauthorized_error() -> None:
    """Test createFhirResourcesMulti endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.create_fhir_resources_multi.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.create_fhir_resources_multi(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_create_fhir_resources_multi_throws_forbidden_error() -> None:
    """Test createFhirResourcesMulti endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.create_fhir_resources_multi.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.create_fhir_resources_multi(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_create_fhir_resources_multi_throws_internal_server_error() -> None:
    """Test createFhirResourcesMulti endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.create_fhir_resources_multi.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.create_fhir_resources_multi(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-create-multi", None, 1)


def test_tools_search_fhir_resources() -> None:
    """Test searchFhirResources endpoint with WireMock"""
    test_id = "tools.search_fhir_resources.0"
    client = get_client(test_id)
    client.tools.search_fhir_resources(
        phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
        phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
        text="Find all appointments for patient John Doe next week",
        count=10,
        provider="550e8400-e29b-41d4-a716-446655440000",
    )
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-search", None, 1)


def test_tools_search_fhir_resources_throws_bad_request_error() -> None:
    """Test searchFhirResources endpoint error response (BadRequestError) with WireMock"""
    test_id = "tools.search_fhir_resources.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tools.search_fhir_resources(
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-search", None, 1)


def test_tools_search_fhir_resources_throws_unauthorized_error() -> None:
    """Test searchFhirResources endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.search_fhir_resources.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.search_fhir_resources(
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-search", None, 1)


def test_tools_search_fhir_resources_throws_forbidden_error() -> None:
    """Test searchFhirResources endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.search_fhir_resources.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.search_fhir_resources(
            text="text",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/lang2fhir-and-search", None, 1)


def test_tools_search_fhir_resources_throws_internal_server_error() -> None:
    """Test searchFhirResources endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.search_fhir_resources.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.search_fhir_resources(
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_tools_analyze_cohort_throws_bad_request_error() -> None:
    """Test analyzeCohort endpoint error response (BadRequestError) with WireMock"""
    test_id = "tools.analyze_cohort.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.tools.analyze_cohort(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/cohort", None, 1)


def test_tools_analyze_cohort_throws_unauthorized_error() -> None:
    """Test analyzeCohort endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "tools.analyze_cohort.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.tools.analyze_cohort(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/cohort", None, 1)


def test_tools_analyze_cohort_throws_forbidden_error() -> None:
    """Test analyzeCohort endpoint error response (ForbiddenError) with WireMock"""
    test_id = "tools.analyze_cohort.3"
    client = get_client(test_id)
    with pytest.raises(ForbiddenError) as exc_info:
        client.tools.analyze_cohort(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 403
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/cohort", None, 1)


def test_tools_analyze_cohort_throws_internal_server_error() -> None:
    """Test analyzeCohort endpoint error response (InternalServerError) with WireMock"""
    test_id = "tools.analyze_cohort.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.tools.analyze_cohort(
            text="text",
            provider="provider",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/tools/cohort", None, 1)
