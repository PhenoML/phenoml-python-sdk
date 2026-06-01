from .conftest import get_client, verify_request_count

from phenoml.construe import ExtractCodesResult, ExtractedCodeResult, ExtractRequestSystem


def test_construe_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "construe.list_.0"
    client = get_client(test_id)
    client.construe.list(
        codesystem="ICD-10-CM",
        version="2025",
        cursor="cursor",
        limit=1,
    )
    verify_request_count(
        test_id, "GET", "/construe/codes/ICD-10-CM", {"version": "2025", "cursor": "cursor", "limit": "1"}, 1
    )


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
