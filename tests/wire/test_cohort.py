import pytest
from .conftest import get_client, verify_request_count

from phenoml.cohort import BadRequestError, InternalServerError, UnauthorizedError
from phenoml.core.jsonable_encoder import jsonable_encoder


def test_cohort_analyze() -> None:
    """Test analyze endpoint with WireMock"""
    test_id = "cohort.analyze.0"
    client = get_client(test_id)
    client.cohort.analyze(
        text="female patients over 65 with diabetes but not hypertension",
    )
    verify_request_count(test_id, "POST", "/cohort", None, 1)


def test_cohort_analyze_throws_bad_request_error() -> None:
    """Test analyze endpoint error response (BadRequestError) with WireMock"""
    test_id = "cohort.analyze.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.cohort.analyze(
            text="text",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/cohort", None, 1)


def test_cohort_analyze_throws_unauthorized_error() -> None:
    """Test analyze endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "cohort.analyze.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.cohort.analyze(
            text="text",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/cohort", None, 1)


def test_cohort_analyze_throws_internal_server_error() -> None:
    """Test analyze endpoint error response (InternalServerError) with WireMock"""
    test_id = "cohort.analyze.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.cohort.analyze(
            text="text",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/cohort", None, 1)
