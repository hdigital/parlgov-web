import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_election_index_redirect(client):
    response = client.get(reverse("elections:index_redirect"))

    assert response.status_code == 302
    assert response.url == "/data/"


def test_election_list(client, db, election):
    response = client.get(reverse("elections:list", kwargs={"country": "deu"}))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/elections/deu/"
    assert "2020-01-01" in response.rendered_content

    assertTemplateUsed(response, "data/election-list.html")


def test_election_list_404(client, db, election):
    response = client.get(reverse("elections:list", kwargs={"country": "ddd"}))

    assert response.status_code == 404
