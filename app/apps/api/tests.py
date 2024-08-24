import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from apps.data.core.models import Country

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


def test_api_auth_disabled(client):
    response = client.get("/api-auth/login/")

    assert response.status_code == 404


def test_api_root(api_client):
    response = api_client.get(reverse("api:api-root"))

    assert response.headers["Allow"] == "GET, HEAD, OPTIONS"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_reverse",
    [
        "api:country-list",
        "api:party-list",
        "api:partychange-list",
        "api:partynamechange-list",
        "api:election-list",
        "api:electionresult-list",
        "api:cabinet-list",
        "api:cabinetparty-list",
        "api:code-list",
    ],
)
def test_api_lists(api_client, url_reverse):
    response = api_client.get(reverse(url_reverse))

    assert response.headers["Allow"] == "GET, HEAD, OPTIONS"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_reverse",
    [
        "api:country-detail",
        "api:party-detail",
        "api:partychange-detail",
        "api:partynamechange-detail",
        "api:election-detail",
        "api:electionresult-detail",
        "api:cabinet-detail",
        "api:cabinetparty-detail",
        "api:code-detail",
    ],
)
def test_api_details(api_client, url_reverse):
    """Test that the detail views are implemented.

    No factories or fixtures are used here, so the response will be 404.
    The purpose of the tests is to ensure that the views are implemented.
    """
    response = api_client.get(reverse(url_reverse, kwargs={"pk": 1}))

    assert response.headers["Allow"] == "GET, HEAD, OPTIONS"
    assert response.status_code == 404
    assert response.reason_phrase == "Not Found"


def test_api_search(api_client, db):
    _ = Country.objects.create(name="Sweden")
    response = api_client.get(reverse("api:country-list"), {"search": "Sweden"})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == "Sweden"
