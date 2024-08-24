from http import HTTPStatus

import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_home_page(client):
    response = client.get(reverse("page:home"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/"
    assert "ParlGov" in response.rendered_content

    assertTemplateUsed(response, "home/home.html")


def test_page_not_found_404(client):
    response = client.get("/random-project-page/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


def test_robots_page(client):
    response = client.get(reverse("page:robots"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/robots.txt"
    assert response["content-type"] == "text/plain"

    assertTemplateUsed(response, "pages/robots.txt")


def test_robots_post_disallowed(client):
    response = client.post("/robots.txt")

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
