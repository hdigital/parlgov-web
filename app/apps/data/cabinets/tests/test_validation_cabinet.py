from datetime import timedelta

import pytest

from django.core.exceptions import ValidationError

from ...core.tests.factories import CountryFactory
from .. import validation
from .factories import CabinetPartyFactory


def test_countries_cabinet_party_equal(db, cabinet_party):
    cabinet_party.party.country = CountryFactory(
        name="Sweden", name_short="SWE", code_iso2="SE"
    )
    with pytest.raises(ValidationError):
        validation.check_cabinet_party_countries(cabinet_party)

    with pytest.raises(ValidationError):
        cabinet_party.clean()


def test_cabinet_election_validation(db, cabinet, cabinet_election):
    cabinet.save()  # update 'cabinet.election' on save

    # change 'election' to date after 'cabinet' start
    cabinet_election.date = cabinet.start_date + timedelta(days=1)
    cabinet_election.save()

    with pytest.raises(ValidationError):
        validation.check_cabinet_election(cabinet)


def test_cabinet_includes_pm(db, cabinet_party):
    assert validation.check_cabinet_includes_pm(cabinet_party.cabinet) is None


def test_cabinet_includes_no_pm_error(db, cabinet_party):
    cabinet_party.pm = False
    cabinet_party.save()

    with pytest.raises(ValidationError):
        validation.check_cabinet_includes_pm(cabinet_party.cabinet)


def test_cabinet_includes_no_pm_switzerland(db, cabinet):
    with pytest.raises(ValidationError):
        validation.check_cabinet_includes_pm(cabinet)

    cabinet.country.name_short = "CHE"
    assert validation.check_cabinet_includes_pm(cabinet) is None


def test_cabinet_includes_single_pm(db, cabinet_party):
    cabinet_party_new = CabinetPartyFactory(id=2)

    with pytest.raises(ValidationError):
        cabinet_party_new.clean()

    with pytest.raises(ValidationError):
        validation.check_cabinet_party_no_second_pm(cabinet_party_new)
