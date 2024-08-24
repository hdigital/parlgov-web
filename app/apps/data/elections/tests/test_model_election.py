from datetime import date

import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse

from ...core.models import Country
from ..models import Election
from .factories import ElectionFactory


def test_election_model(db, election):
    assert str(election) == "Election Deu – 2020 (1)"

    assert election.date == date(2020, 1, 1)


def test_election_admin(admin_client):
    response = admin_client.get(reverse("admin:elections_election_add"))
    assert response.status_code == 200


@pytest.mark.parametrize(
    "field", ["seats_total", "electorate", "votes_cast", "votes_valid"]
)
def test_field_not_negative(db, election, field):
    setattr(election, field, -1)
    with pytest.raises(IntegrityError):
        election.save()


def test_seats_total_maximum(db, election):
    election.seats_total = 1500
    with pytest.raises(ValidationError):
        election.full_clean()


def test_date_unique(db, election):
    election_two = ElectionFactory(date="1999-09-09")
    with pytest.raises(ValidationError):
        election_two.date = election.date
        election_two.full_clean()


def test_get_previous_election(db):
    election = ElectionFactory(date="2000-01-01")
    election.save()

    assert Election.get_by_date(election.country, "1999-01-01") is None
    assert Election.get_by_date(election.country, election.date) == election
    assert Election.get_by_date(election.country, "2001-01-01") == election

    other_country = Country(name_short="NOR")
    other_country.save()
    assert Election.get_by_date(other_country, election.date) != election


def test_ep_name(db, election_ep):
    assert " EP (" in str(election_ep)


def test_absolute_url_parliament(db, election):
    assert election.get_absolute_url() == "/data/elections/deu/2020-01-01/"


def test_absolute_url_ep(db, election_ep):
    assert election_ep.get_absolute_url() == "/data/elections/deu/2020-01-01-ep/"
