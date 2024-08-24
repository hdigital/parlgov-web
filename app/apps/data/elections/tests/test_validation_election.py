from datetime import date

import pytest

from django.core.exceptions import ValidationError

from ...core.tests.factories import CountryFactory
from .. import validation
from .factories import ElectionFactory, ElectionResultFactory


def test_election_includes_result(db, election):
    with pytest.raises(ValidationError):
        validation.check_election_includes_result(election)

    _ = ElectionResultFactory(election=election)
    assert validation.check_election_includes_result(election) is None


def test_countries_election_party_equal(db, election_result):
    election_result.party.country = CountryFactory(
        name="Sweden", name_short="SWE", code_iso2="SE"
    )
    with pytest.raises(ValidationError):
        validation.check_election_party_countries(election_result)

    with pytest.raises(ValidationError):
        election_result.clean()


def test_alliance_no_self_reference(db, election_result):
    election_result.alliance = election_result

    with pytest.raises(ValidationError):
        validation.check_alliance_no_self_reference(election_result)

    with pytest.raises(ValidationError):
        election_result.clean()


def test_alliance_election_ids_not_equal(db, election_result):
    election_new = ElectionFactory(date=date(1900, 1, 1))
    election_result_new = ElectionResultFactory(election=election_new)

    election_result.alliance = election_result_new

    with pytest.raises(ValidationError):
        validation.check_alliance_election_ids_equal(election_result)

    with pytest.raises(ValidationError):
        election_result.clean()


def test_includes_no_seats_party(db, election_result):
    election = election_result.election

    with pytest.raises(ValidationError):
        validation.check_no_seats_party(election)

    _ = ElectionResultFactory(election=election, seats=0)

    validation.check_no_seats_party(election)


def test_one_percent_vote_share(db, election):
    _ = ElectionResultFactory(election=election, seats=0, vote_share=0.5)
    _ = ElectionResultFactory(election=election, seats=0, vote_share=0.5)

    with pytest.raises(ValidationError):
        validation.check_one_percent_vote_share(election)


def test_seats_sum_seats_total(db, election):
    _ = ElectionResultFactory(election=election, seats=10)
    _ = ElectionResultFactory(election=election, seats=20)

    election.seats_total = 50

    with pytest.raises(ValidationError):
        validation.check_seats_sum(election)


@pytest.mark.parametrize("share", [0, 85, 101])
def test_vote_share_sum_valid(db, election, share):
    _ = ElectionResultFactory(election=election, vote_share=share)

    assert validation.check_vote_share_sum(election) is None


@pytest.mark.parametrize("share", [84.9, 102.1])
def test_vote_share_sum_invalid(db, election, share):
    _ = ElectionResultFactory(election=election, vote_share=share)

    with pytest.raises(ValidationError):
        validation.check_vote_share_sum(election)


def test_vote_share_sum_checked(db, election):
    election.data_json = {"vote_share_sum": True}

    assert validation.check_vote_share_sum(election) is None
