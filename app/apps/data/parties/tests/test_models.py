import re
from datetime import date

import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse

from ...core.tests.factories import CountryFactory
from .factories import PartyChangeFactory, PartyFactory, PartyNameChangeFactory


@pytest.fixture
def party_name_change():
    """A 'PartyNameChange' object with default values."""
    return PartyNameChangeFactory()


@pytest.fixture
def party_change():
    """A 'PartyChange' object with default values."""
    return PartyChangeFactory()


def test_name_change_model(db, party_name_change):
    assert re.match(r"PartyNameChange Deu — Gru(\d+) \(1\)", str(party_name_change))
    assert party_name_change.family == party_name_change.party.family

    assert party_name_change.full_clean() is None
    assert party_name_change.name_short == "Gru"


def test_name_change_admin(admin_client):
    response = admin_client.get(reverse("admin:parties_partynamechange_add"))
    assert response.status_code == 200


def test_name_change_date_clean(db, party_name_change):
    party_name_change.date = date(1980, 7, 1)
    assert party_name_change.date_clean == "1980"

    party_name_change.date = date(1980, 2, 1)
    assert party_name_change.date_clean == "1980-02"


def test_change_model(db, party_change):
    assert re.match(r"PartyChange Deu — Gru(\d+) // Gru(\d+) \(1\)", str(party_change))
    assert party_change.party != party_change.party_new


def test_change_admin(admin_client):
    response = admin_client.get(reverse("admin:parties_partychange_add"))
    assert response.status_code == 200


def test_change_parties_unique(db, party):
    with pytest.raises(IntegrityError):
        _ = PartyChangeFactory(party=party, party_new=party)


def test_change_countries_equal(db, party):
    party_new = PartyFactory()
    party_new.country = CountryFactory(name="Sweden", name_short="SWE", code_iso2="SE")

    with pytest.raises(ValidationError):
        party_change = PartyChangeFactory(party=party, party_new=party_new)
        party_change.clean()


def test_change_date_clean(db, party_change):
    party_change.date = date(2000, 7, 1)
    assert party_change.date_clean == "2000"

    party_change.date = date(2000, 9, 1)
    assert party_change.date_clean == "2000-09"


def test_change_related_names(db, party_change):
    assert party_change.party.partychange_set.exists()
    assert party_change.party_new.partychange_new_set.exists()
