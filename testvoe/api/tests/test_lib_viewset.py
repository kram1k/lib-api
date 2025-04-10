import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from libraries.models import Library
from api.serializers import LibrarySerializer

pytestmark = pytest.mark.django_db


@pytest.fixture
def library():
    return Library.objects.create(
        full_name="Test Library",
        region="Test Region",
        address="Test Address",
        year=2023,
        inter_budget_transfer_amount=1000000,
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        password="testpassword",
    )


@pytest.fixture
def authenticated_api_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


def test_library_list(api_client):
    url = reverse("api:library-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_library_create(authenticated_api_client):
    url = reverse("api:library-list")
    data = {
        "full_name": "Test Library",
        "region": "Test Region",
        "address": "Test Address",
        "year": 2023,
        "inter_budget_transfer_amount": 1000000,
    }
    response = authenticated_api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Library.objects.count() == 1
    library = Library.objects.first()
    assert library.full_name == "Test Library"


def test_library_retrieve(api_client, library):
    url = reverse("api:library-detail", kwargs={"pk": library.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    serializer = LibrarySerializer(library)
    assert response.data == serializer.data


def test_library_update(authenticated_api_client, library):
    url = reverse("api:library-detail", kwargs={"pk": library.pk})
    data = {
        "full_name": "Updated Library Name",
        "region": library.region,
        "address": library.address,
        "year": library.year,
        "inter_budget_transfer_amount": library.inter_budget_transfer_amount,
    }
    response = authenticated_api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    library.refresh_from_db()
    assert library.full_name == "Updated Library Name"


def test_library_delete(authenticated_api_client, library):
    url = reverse("api:library-detail", kwargs={"pk": library.pk})
    response = authenticated_api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Library.objects.count() == 0


def test_library_filter_by_full_name(api_client, library):
    url = reverse("api:library-list") + f"?full_name={library.full_name}"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["full_name"] == library.full_name
