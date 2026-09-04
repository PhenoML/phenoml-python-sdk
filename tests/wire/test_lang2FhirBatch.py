from .conftest import get_client, verify_request_count


def test_lang2FhirBatch_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "lang2fhir_batch.list_.0"
    client = get_client(test_id)
    client.lang2fhir_batch.list(
        cursor="cursor",
        limit=1,
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch", {"cursor": "cursor", "limit": "1"}, 1)


def test_lang2FhirBatch_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "lang2fhir_batch.create.0"
    client = get_client(test_id)
    client.lang2fhir_batch.create(
        request_id="submit-2025-09-02-batch-001",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_upload_item() -> None:
    """Test uploadItem endpoint with WireMock"""
    test_id = "lang2fhir_batch.upload_item.0"
    client = get_client(test_id)
    client.lang2fhir_batch.upload_item(
        job_id="job_id",
        file="example_file",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/items", None, 1)


def test_lang2FhirBatch_finalize() -> None:
    """Test finalize endpoint with WireMock"""
    test_id = "lang2fhir_batch.finalize.0"
    client = get_client(test_id)
    client.lang2fhir_batch.finalize(
        job_id="job_id",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "lang2fhir_batch.get.0"
    client = get_client(test_id)
    client.lang2fhir_batch.get(
        job_id="job_id",
        cursor="cursor",
        limit=1,
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", {"cursor": "cursor", "limit": "1"}, 1)


def test_lang2FhirBatch_get_results() -> None:
    """Test getResults endpoint with WireMock"""
    test_id = "lang2fhir_batch.get_results.0"
    client = get_client(test_id)
    client.lang2fhir_batch.get_results(
        job_id="job_id",
        cursor="cursor",
        limit=1,
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", {"cursor": "cursor", "limit": "1"}, 1)


def test_lang2FhirBatch_get_result() -> None:
    """Test getResult endpoint with WireMock"""
    test_id = "lang2fhir_batch.get_result.0"
    client = get_client(test_id)
    client.lang2fhir_batch.get_result(
        job_id="job_id",
        item_id="item_id",
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)
