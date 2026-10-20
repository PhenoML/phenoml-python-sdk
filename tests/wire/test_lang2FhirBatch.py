import pytest
from .conftest import get_client, verify_request_count

from phenoml.core.jsonable_encoder import jsonable_encoder
from phenoml.lang2fhir_batch import (
    BadRequestError,
    ClientClosedRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


def test_lang2FhirBatch_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "lang2fhir_batch.list_.0"
    client = get_client(test_id)
    client.lang2fhir_batch.list(
        cursor="cursor",
        limit=1,
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch", {"cursor": "cursor", "limit": "1"}, 1)


def test_lang2FhirBatch_list__throws_bad_request_error() -> None:
    """Test list endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.list_.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.list()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_list__throws_unauthorized_error() -> None:
    """Test list endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.list_.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.list()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_list__throws_client_closed_request_error() -> None:
    """Test list endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.list_.3"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.list()
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_list__throws_internal_server_error() -> None:
    """Test list endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.list_.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.list()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_list__throws_gateway_timeout_error() -> None:
    """Test list endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.list_.5"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.list()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "lang2fhir_batch.create.0"
    client = get_client(test_id)
    client.lang2fhir_batch.create(
        request_id="submit-2025-09-02-batch-001",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create_throws_bad_request_error() -> None:
    """Test create endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.create.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.create()
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create_throws_unauthorized_error() -> None:
    """Test create endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.create.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.create()
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create_throws_client_closed_request_error() -> None:
    """Test create endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.create.3"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.create()
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create_throws_internal_server_error() -> None:
    """Test create endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.create.4"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.create()
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch", None, 1)


def test_lang2FhirBatch_create_throws_gateway_timeout_error() -> None:
    """Test create endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.create.5"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.create()
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
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


def test_lang2FhirBatch_finalize_throws_bad_request_error() -> None:
    """Test finalize endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_unauthorized_error() -> None:
    """Test finalize endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_not_found_error() -> None:
    """Test finalize endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_conflict_error() -> None:
    """Test finalize endpoint error response (ConflictError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.4"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_client_closed_request_error() -> None:
    """Test finalize endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.5"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_internal_server_error() -> None:
    """Test finalize endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_finalize_throws_gateway_timeout_error() -> None:
    """Test finalize endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.finalize.7"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.finalize(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/finalize", None, 1)


def test_lang2FhirBatch_cancel() -> None:
    """Test cancel endpoint with WireMock"""
    test_id = "lang2fhir_batch.cancel.0"
    client = get_client(test_id)
    client.lang2fhir_batch.cancel(
        job_id="job_id",
    )
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_unauthorized_error() -> None:
    """Test cancel endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.1"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_not_found_error() -> None:
    """Test cancel endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.2"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_conflict_error() -> None:
    """Test cancel endpoint error response (ConflictError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.3"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_client_closed_request_error() -> None:
    """Test cancel endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.4"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_internal_server_error() -> None:
    """Test cancel endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


def test_lang2FhirBatch_cancel_throws_gateway_timeout_error() -> None:
    """Test cancel endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.cancel.6"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.cancel(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "POST", "/lang2fhir/batch/job_id/cancel", None, 1)


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


def test_lang2FhirBatch_get_throws_bad_request_error() -> None:
    """Test get endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


def test_lang2FhirBatch_get_throws_unauthorized_error() -> None:
    """Test get endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.get.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


def test_lang2FhirBatch_get_throws_not_found_error() -> None:
    """Test get endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir_batch.get.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


def test_lang2FhirBatch_get_throws_client_closed_request_error() -> None:
    """Test get endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get.4"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


def test_lang2FhirBatch_get_throws_internal_server_error() -> None:
    """Test get endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.get.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


def test_lang2FhirBatch_get_throws_gateway_timeout_error() -> None:
    """Test get endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.get.6"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.get(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id", None, 1)


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


def test_lang2FhirBatch_get_results_throws_bad_request_error() -> None:
    """Test getResults endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_results_throws_unauthorized_error() -> None:
    """Test getResults endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_results_throws_not_found_error() -> None:
    """Test getResults endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_results_throws_client_closed_request_error() -> None:
    """Test getResults endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.4"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_results_throws_internal_server_error() -> None:
    """Test getResults endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.5"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_results_throws_gateway_timeout_error() -> None:
    """Test getResults endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.get_results.6"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.get_results(
            job_id="job_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results", None, 1)


def test_lang2FhirBatch_get_result() -> None:
    """Test getResult endpoint with WireMock"""
    test_id = "lang2fhir_batch.get_result.0"
    client = get_client(test_id)
    client.lang2fhir_batch.get_result(
        job_id="job_id",
        item_id="item_id",
    )
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_bad_request_error() -> None:
    """Test getResult endpoint error response (BadRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_unauthorized_error() -> None:
    """Test getResult endpoint error response (UnauthorizedError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.2"
    client = get_client(test_id)
    with pytest.raises(UnauthorizedError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 401
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_not_found_error() -> None:
    """Test getResult endpoint error response (NotFoundError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.3"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_conflict_error() -> None:
    """Test getResult endpoint error response (ConflictError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.4"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_client_closed_request_error() -> None:
    """Test getResult endpoint error response (ClientClosedRequestError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.5"
    client = get_client(test_id)
    with pytest.raises(ClientClosedRequestError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 499
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_internal_server_error() -> None:
    """Test getResult endpoint error response (InternalServerError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.6"
    client = get_client(test_id)
    with pytest.raises(InternalServerError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 500
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)


def test_lang2FhirBatch_get_result_throws_gateway_timeout_error() -> None:
    """Test getResult endpoint error response (GatewayTimeoutError) with WireMock"""
    test_id = "lang2fhir_batch.get_result.7"
    client = get_client(test_id)
    with pytest.raises(GatewayTimeoutError) as exc_info:
        client.lang2fhir_batch.get_result(
            job_id="job_id",
            item_id="item_id",
        )
    assert exc_info.value.status_code == 504
    assert jsonable_encoder(exc_info.value.body) == {"key": "value"}
    verify_request_count(test_id, "GET", "/lang2fhir/batch/job_id/results/item_id", None, 1)
