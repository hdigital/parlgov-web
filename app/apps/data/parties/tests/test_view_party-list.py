import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_party_index_redirect(client):
    response = client.get(reverse("parties:index_redirect"))

    assert response.status_code == 302
    assert response.url == "/data/"


def test_party_list(client, db, party):
    response = client.get(reverse("parties:list", kwargs={"country": "deu"}))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/parties/deu/"
    assert "Greens" in response.rendered_content

    assertTemplateUsed(response, "data/party-list.html")


def test_party_list_404(client, db, party):
    response = client.get(reverse("parties:list", kwargs={"country": "ddd"}))

    assert response.status_code == 404
