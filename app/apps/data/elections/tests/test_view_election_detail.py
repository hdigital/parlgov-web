import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ...cabinets.tests.factories import CabinetPartyFactory
from .factories import ElectionFactory

pytestmark = pytest.mark.django_db


def get_election_detail_response(client, election_result):
    response = client.get(
        reverse(
            "elections:detail",
            kwargs={
                "country": election_result.election.country.slug,
                "election_date": election_result.election.date.strftime("%Y-%m-%d"),
            },
        )
    )
    return response


def get_election_ep_detail_response(client, election_ep):
    response = client.get(
        reverse(
            "elections:detail_ep",
            kwargs={
                "country": election_ep.country.slug,
                "election_date": election_ep.date,
            },
        )
    )
    return response


def test_election_detail(client, db, election_result):
    response = get_election_detail_response(client, election_result)

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/elections/deu/2020-01-01/"

    assert "1. January 2020" in response.rendered_content
    assert "<!-- cabinets-section-test -->" not in response.rendered_content

    assertTemplateUsed(response, "data/election-detail.html")


def test_election_ep_detail(client, db, election_ep):
    response = get_election_ep_detail_response(client, election_ep)

    assert response.status_code == 200
    assert (
        response.request["PATH_INFO"] == f"/data/elections/deu/{election_ep.date}-ep/"
    )


def test_election_ep_detail_previous_election(client, db, election_ep):
    """Test that EP election page includes the previous parliamentary election."""
    _ = ElectionFactory(country=election_ep.country, date="1999-01-01")

    response = get_election_ep_detail_response(client, election_ep)

    assert response.status_code == 200
    assert "Election parliament" in response.rendered_content
    assert "1. January 1999" in response.rendered_content


def test_election_detail_404(client, db):
    response = client.get(
        reverse(
            "elections:detail",
            kwargs={"country": "ddd", "election_date": "1900-09-09"},
        )
    )

    assert response.status_code == 404


def test_round_vote_share(client, db, election_result):
    election_result.vote_share = 88.88
    election_result.save()

    response = get_election_detail_response(client, election_result)

    assert "88.9" in response.rendered_content


def test_election_detail_cabinet(client, db, election_result):
    _ = CabinetPartyFactory()

    response = get_election_detail_response(client, election_result)

    assert "<!-- cabinets-section-test -->" in response.rendered_content
