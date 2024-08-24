from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ...elections.tests.factories import ElectionFactory


def test_cabinet_detail(client, db, cabinet_party):
    kw_args = {"country": "deu", "cabinet_date": "2021-07-01"}
    response = client.get(reverse("cabinets:detail", kwargs=kw_args))

    assert response.status_code == 200

    assert response.request["PATH_INFO"] == "/data/cabinets/deu/2021-07-01/"
    assert "1. July 2021" in response.rendered_content
    assert "Gru" in response.rendered_content

    assertTemplateUsed(response, "data/cabinet-detail.html")


def test_cabinet_detail_404(client, db, cabinet_party):
    kw_args = {"country": "ddd", "cabinet_date": "2000-01-01"}
    response = client.get(reverse("cabinets:detail", kwargs=kw_args))

    assert response.status_code == 404


def test_cabinet_election(client, db, cabinet_party):
    _ = ElectionFactory(country__short="DEU", date="2000-01-01")
    cabinet_party.cabinet.save()  # set 'self.election' attribute on save

    kw_args = {"country": "deu", "cabinet_date": "2021-07-01"}
    response = client.get(reverse("cabinets:detail", kwargs=kw_args))

    assert response.status_code == 200
    assert "1. January 2000" in response.rendered_content
