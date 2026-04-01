from .conftest import get_client, verify_request_count


def test_cohort_analyze() -> None:
    """Test analyze endpoint with WireMock"""
    test_id = "cohort.analyze.0"
    client = get_client(test_id)
    client.cohort.analyze(text="female patients over 65 with diabetes but not hypertension")
    verify_request_count(test_id, "POST", "/cohort", None, 1)
