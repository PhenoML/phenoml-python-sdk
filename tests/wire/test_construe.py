import pytest
from .conftest import get_client, verify_request_count

from phenoml.construe import (
    BadRequestError,
    ExtractCodesResult,
    ExtractedCodeResult,
    ExtractRequestSystem,
    InternalServerError,
    ServiceUnavailableError,
    UnauthorizedError,
)
from phenoml.core.jsonable_encoder import jsonable_encoder


def test_construe_submit_feedback() -> None:
    """Test submitFeedback endpoint with WireMock"""
    test_id = "construe.submit_feedback.0"
    client = get_client(test_id)
    client.construe.submit_feedback(
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


def test_construe_submit_feedback_throws_bad_request_error() -> None:
    """Test submitFeedback endpoint error response (BadRequestError) with WireMock"""
    test_id = "construe.submit_feedback.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.construe.submit_feedback(
            text="text",
            received_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
            expected_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/feedback", None, 1)


def test_construe_submit_feedback_throws_unauthorized_error() -> None:
    """Test submitFeedback endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "construe.submit_feedback.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.construe.submit_feedback(
            text="text",
            received_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
            expected_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/feedback", None, 1)


def test_construe_submit_feedback_throws_internal_server_error() -> None:
    """Test submitFeedback endpoint error response (InternalServerError) with WireMock"""
    test_id = "construe.submit_feedback.3"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.construe.submit_feedback(
            text="text",
            received_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
            expected_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/feedback", None, 1)


def test_construe_submit_feedback_throws_service_unavailable_error() -> None:
    """Test submitFeedback endpoint error response (ServiceUnavailableError) with WireMock"""
    test_id = "construe.submit_feedback.4"
    client = get_client(test_id)
    with pytest.raises(ServiceUnavailableError) as exc_info:
        client.construe.submit_feedback(
            text="text",
            received_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
            expected_result=ExtractCodesResult(
                system=ExtractRequestSystem(),
                codes=[
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                    ExtractedCodeResult(
                        code="code",
                        description="description",
                        valid=True,
                    ),
                ],
            ),
        )
    assert exc_info.value.status_code == 503
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/construe/feedback", None, 1)
