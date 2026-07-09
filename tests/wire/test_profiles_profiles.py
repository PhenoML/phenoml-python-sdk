from .conftest import get_client, verify_request_count


def test_profiles_profiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "profiles.profiles.list_.0"
    client = get_client(test_id)
    client.profiles.profiles.list(
        url="http://phenoml.com/fhir/StructureDefinition/custom-patient|1.0.0",
    )
    verify_request_count(
        test_id, "GET", "/fhir/profiles", {"url": "http://phenoml.com/fhir/StructureDefinition/custom-patient|1.0.0"}, 1
    )


def test_profiles_profiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "profiles.profiles.create.0"
    client = get_client(test_id)
    client.profiles.profiles.create(
        structure_definition={"key": "value"},
    )
    verify_request_count(test_id, "POST", "/fhir/profiles", None, 1)


def test_profiles_profiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "profiles.profiles.get.0"
    client = get_client(test_id)
    client.profiles.profiles.get(
        id="custom-patient",
    )
    verify_request_count(test_id, "GET", "/fhir/profiles/custom-patient", None, 1)


def test_profiles_profiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "profiles.profiles.update.0"
    client = get_client(test_id)
    client.profiles.profiles.update(
        id="custom-patient",
        structure_definition={"key": "value"},
    )
    verify_request_count(test_id, "PUT", "/fhir/profiles/custom-patient", None, 1)


def test_profiles_profiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "profiles.profiles.delete.0"
    client = get_client(test_id)
    client.profiles.profiles.delete(
        id="custom-patient",
    )
    verify_request_count(test_id, "DELETE", "/fhir/profiles/custom-patient", None, 1)
