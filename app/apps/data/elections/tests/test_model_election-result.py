import re

import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse

from .factories import ElectionResultFactory


def test_election_result_model(db, election_result):
    assert re.match(r"Election result Deu – 2020 Gru(\d+) \(1\)", str(election_result))

    assert election_result.seats == 10


def test_election_result_admin(admin_client):
    response = admin_client.get(reverse("admin:elections_electionresult_add"))
    assert response.status_code == 200


def test_absolute_url(db, election_result):
    result_url = election_result.get_absolute_url()
    election_url = election_result.election.get_absolute_url()

    assert result_url == election_url


@pytest.mark.parametrize("field", ["seats", "vote_share", "votes"])
def test_field_not_negative(db, election_result, field):
    setattr(election_result, field, -1)
    with pytest.raises((IntegrityError, ValidationError)):
        election_result.full_clean()
        election_result.save()


def test_party_unique(db, election_result):
    with pytest.raises(IntegrityError):
        _ = ElectionResultFactory(party=election_result.party)


def test_alliance_self_reference(db, election_result):
    alliance_member = ElectionResultFactory(
        election=election_result.election, alliance=election_result
    )

    assert alliance_member.alliance == election_result
    assert election_result.alliance_set.all().first() == alliance_member


@pytest.mark.parametrize("share", [-1, 101, 0.123])
def test_vote_share_invalid(db, election_result, share):
    election_result.vote_share = share
    with pytest.raises(ValidationError):
        election_result.full_clean()


def test_seat_share(db, election_result):
    seat_share = election_result.seats / election_result.election.seats_total * 100

    assert seat_share == election_result.seat_share
