from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_cabinet_index_redirect(client):
    response = client.get(reverse("cabinets:index_redirect"))

    assert response.status_code == 302
    assert response.url == "/data/"


def test_cabinet_list(client, db, cabinet):
    response = client.get(reverse("cabinets:list", kwargs={"country": "deu"}))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/cabinets/deu/"
    assert "2021-07-01" in response.rendered_content

    assertTemplateUsed(response, "data/cabinet-list.html")


def test_cabinet_list_404(client, db, cabinet):
    response = client.get(reverse("cabinets:list", kwargs={"country": "ddd"}))

    assert response.status_code == 404
