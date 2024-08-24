from datetime import date

import pytest

from django.core.exceptions import ValidationError

from ...cabinets.tests.factories import CabinetPartyFactory
from ...core.tests.factories import CodeFactory
from ...elections.tests.factories import ElectionFactory, ElectionResultFactory
from ...parties.tests.factories import PartyFactory
from .. import validation


def test_party_factory_no_result(db, party):
    """Test party factory without election result raises validation error."""
    with pytest.raises(ValidationError):
        validation.party_include_checks(party)


def test_alliance(db, party):
    result_one = ElectionResultFactory(party=party)
    _ = ElectionResultFactory(alliance=result_one)

    election_two = ElectionFactory(date=date(2021, 1, 1))
    result_two = ElectionResultFactory(election=election_two, party=party)
    _ = ElectionResultFactory(election=election_two, alliance=result_two)

    assert validation.check_alliance(party)


def test_alliance_member(db, party):
    alliance_party = PartyFactory()

    result_one = ElectionResultFactory(party=alliance_party)
    _ = ElectionResultFactory(party=party, alliance=result_one)

    election_two = ElectionFactory(date=date(2021, 1, 1))
    result_two = ElectionResultFactory(election=election_two, party=alliance_party)
    _ = ElectionResultFactory(election=election_two, party=party, alliance=result_two)

    assert validation.check_alliance_member(party)


def test_cabinet_party(db, party):
    _ = CabinetPartyFactory(party=party)

    assert validation.check_cabinet_party(party)


def test_json_include(db):
    party = PartyFactory(data_json={"include": "inclusion criteria"})

    assert validation.check_json_include(party)


def test_no_party(db):
    family_none = CodeFactory(table_variable="party_family", short="none")
    party = PartyFactory(family=family_none)

    assert validation.check_no_party(party)


def test_seats(db, party):
    _ = ElectionResultFactory(party=party, vote_share=None, seats=2)

    assert validation.check_seats(party)


def test_seats_json(db, party):
    _ = ElectionResultFactory(
        party=party, vote_share=None, seats=None, data_json={"seats": 2}
    )

    assert validation.check_seats_json(party)


def test_seats_sum(db, party):
    _ = ElectionResultFactory(party=party, vote_share=None, seats=1)
    election_two = ElectionFactory(date=date(2021, 1, 1))
    _ = ElectionResultFactory(
        election=election_two, party=party, vote_share=None, seats=1
    )

    assert validation.check_seats_sum(party)


@pytest.mark.parametrize(
    "vote_share, included",
    [
        (0.8, False),
        (0.95, False),
        (0.951, False),  # rounded to two decimal places in model
        (0.956, True),
        (0.96, True),
        (1.0, True),
    ],
)
def test_vote_share(db, party, vote_share, included):
    _ = ElectionResultFactory(party=party, vote_share=vote_share, seats=0)

    assert validation.check_vote_share(party) is included


def test_run_include_checks(db, party):
    _ = ElectionResultFactory(party=party, vote_share=0, seats=2)

    assert validation.run_include_checks(party) == "seats"


def test_party_include_checks(db, party):
    _ = ElectionResultFactory(party=party, vote_share=1.0, seats=0)

    assert validation.party_include_checks(party) is None
