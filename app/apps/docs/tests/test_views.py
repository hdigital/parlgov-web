from datetime import date

import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_docs_index(client):
    response = client.get(reverse("docs:index"))

    assert response.status_code == 302
    assert response.url == "/docs/codebook/"


def test_codebook_page(client):
    response = client.get(reverse("docs:codebook"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/docs/codebook/"
    assert '<h1 id="codebook">Codebook</h1>' in response.rendered_content

    assertTemplateUsed(response, "docs/codebook.html")


def test_codebook_markdown_page(client):
    response = client.get(reverse("docs:codebook_markdown"))

    assert response.status_code == 200
    assert response["Content-Type"] == "text/plain; charset=utf-8"

    assert response.request["PATH_INFO"] == "/docs/codebook-markdown/"
    assert "# ParlGov Codebook" in response.content.decode()

    assertTemplateUsed(response, "docs/codebook-markdown.txt")


def test_news_list(client, news):
    response = client.get(reverse("docs:news"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/docs/news/"
    assert "ParlGov is here" in response.rendered_content

    assertTemplateUsed(response, "docs/news.html")


def test_news_list_date(client, news):
    response = client.get(reverse("docs:news"))

    assert "Jan. 1, 2020" in response.rendered_content
    assert "Jan. 01, 2020" not in response.rendered_content


def test_news_change_date(client, news):
    news.date = date(1912, 12, 12)
    news.save()
    response = client.get(reverse("docs:news"))
    assert "Dec. 12, 1912" in response.rendered_content
