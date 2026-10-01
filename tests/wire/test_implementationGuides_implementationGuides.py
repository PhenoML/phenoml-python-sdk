from .conftest import get_client, verify_request_count

from phenoml.implementation_guides import FhirImplementationGuide


def test_implementationGuides_implementationGuides_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.list_.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.list()
    verify_request_count(test_id, "GET", "/fhir/implementation-guides", None, 1)


def test_implementationGuides_implementationGuides_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.get.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.get(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.update.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.update(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "PUT", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.delete.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.delete(
        name="acme-cardiology",
    )
    verify_request_count(test_id, "DELETE", "/fhir/implementation-guides/acme-cardiology", None, 1)


def test_implementationGuides_implementationGuides_create_version() -> None:
    """Test createVersion endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.create_version.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.create_version(
        name="name",
        implementation_guide=FhirImplementationGuide(
            resource_type="ImplementationGuide",
            url="url",
            version="version",
        ),
        profile_refs=["profile_refs"],
    )
    verify_request_count(test_id, "POST", "/fhir/implementation-guides/name/versions", None, 1)


def test_implementationGuides_implementationGuides_get_version() -> None:
    """Test getVersion endpoint with WireMock"""
    test_id = "implementation_guides.implementation_guides.get_version.0"
    client = get_client(test_id)
    client.implementation_guides.implementation_guides.get_version(
        name="name",
        version="1.0.0",
    )
    verify_request_count(test_id, "GET", "/fhir/implementation-guides/name/versions/1.0.0", None, 1)
