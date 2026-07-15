import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ...cabinets.tests.factories import CabinetPartyFactory
from ...elections.tests.factories import ElectionFactory, ElectionResultFactory

pytestmark = pytest.mark.django_db


KWARGS_DEU_ID_1 = kwargs = {"country": "deu", "party_id": 1}


def test_party_detail(client, db, party):
    response = client.get(reverse("parties:detail", kwargs=KWARGS_DEU_ID_1))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/parties/deu/1/"
    assert "Greens" in response.rendered_content

    assertTemplateUsed(response, "data/party-detail.html")


def test_party_detail_404(client, db, party):
    response = client.get(
        reverse("parties:detail", kwargs={"country": "deu", "party_id": 9999})
    )
    assert response.status_code == 404

    response = client.get(
        reverse("parties:detail", kwargs={"country": "ddd", "party_id": 1})
    )
    assert response.status_code == 404


def test_party_detail_sections(client, db, party):
    response = client.get(reverse("parties:detail", kwargs=KWARGS_DEU_ID_1))

    assert "<!-- elections-section-test -->" not in response.rendered_content
    assert "<!-- elections-ep-section-test -->" not in response.rendered_content
    assert "<!-- cabinets-section-test -->" not in response.rendered_content


def test_party_detail_section_election(client, db, party):
    _ = ElectionResultFactory(party=party)

    response = client.get(reverse("parties:detail", kwargs=KWARGS_DEU_ID_1))

    assert "<!-- elections-section-test -->" in response.rendered_content


def test_party_detail_section_election_ep(client, db, party):
    election_ep = ElectionFactory(type__short="ep")
    _ = ElectionResultFactory(election=election_ep, party=party)

    response = client.get(reverse("parties:detail", kwargs=KWARGS_DEU_ID_1))

    assert "<!-- elections-ep-section-test -->" in response.rendered_content


def test_party_detail_section_cabinet(client, db, party):
    _ = CabinetPartyFactory(party=party)

    response = client.get(reverse("parties:detail", kwargs=KWARGS_DEU_ID_1))

    assert "<!-- cabinets-section-test -->" in response.rendered_content
