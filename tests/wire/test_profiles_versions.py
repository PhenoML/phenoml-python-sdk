from .conftest import get_client, verify_request_count


def test_profiles_versions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "profiles.versions.list_.0"
    client = get_client(test_id)
    client.profiles.versions.list(
        id="custom-patient",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient/versions", None, 1)


def test_profiles_versions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "profiles.versions.create.0"
    client = get_client(test_id)
    client.profiles.versions.create(
        id="custom-patient",
        request={"key": "value"},
    )
    verify_request_count(test_id, "POST", "/fhir/profiles/custom-patient/versions", None, 1)


def test_profiles_versions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "profiles.versions.get.0"
    client = get_client(test_id)
    client.profiles.versions.get(
        id="custom-patient",
        version="2.0.0",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient/versions/2.0.0", None, 1)


def test_profiles_versions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "profiles.versions.delete.0"
    client = get_client(test_id)
    client.profiles.versions.delete(
        id="custom-patient",
        version="2.0.0",
    )
    verify_request_count(test_id, "DELETE", "/fhir/profiles/custom-patient/versions/2.0.0", None, 1)
