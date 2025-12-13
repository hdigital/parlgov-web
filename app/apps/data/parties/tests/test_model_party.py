import re
from datetime import date

import pytest

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse

from ...core.tests.factories import CodeFactory
from ...elections.tests.factories import ElectionResultFactory
from .factories import PartyFactory, PartyFamilyFactory, PartyNameChangeFactory


def test_party_model(db, party):
    assert re.match(r"Party Deu — Gru(\d+) \(1\)", str(party))
    assert party.full_clean() is None
    assert re.match(r"Gru(\d+)", party.name_short)


def test_party_admin(admin_client):
    response = admin_client.get(reverse("admin:parties_party_add"))
    assert response.status_code == 200


def test_absolute_url(db, party):
    assert party.get_absolute_url() == "/data/parties/deu/1/"


def test_party_family_main(db, party):
    family = CodeFactory(table_variable="party_family", order=200)
    party = PartyFactory(family=family)

    with pytest.raises(ValidationError):
        party.full_clean()


def test_name_short_unique(db, party):
    with pytest.raises(IntegrityError):
        _ = PartyFactory(country=party.country, name_short=party.name_short)


@pytest.mark.parametrize("field", ["name_short", "name_english", "name_ascii"])
def test_names_ascii(db, party, field):
    setattr(party, field, "ÄÖÜ")
    with pytest.raises(ValidationError):
        party.full_clean()


def test_name_short_no_space(db, party):
    party.name_short = "A B"
    with pytest.raises(ValidationError):
        party.full_clean()


def test_include_rule(db, party):
    _ = ElectionResultFactory(party=party, vote_share=1.0, seats=0)
    assert party.get_include_rule() == "vote_share"


def test_name_by_date(db, party):
    name_party = party.get_name_by_date(date(1985, 1, 1))
    assert re.match(r"Gru(\d+)", name_party.name_short)

    change_first = PartyNameChangeFactory(date=date(1980, 1, 1), name_short="Gr")
    party.partynamechange_set.add(change_first)
    name_first = party.get_name_by_date(date(1985, 1, 1))
    assert name_first.name_short == change_first.name_short

    change_second = PartyNameChangeFactory(date=date(1990, 1, 1), name_short="B90/Gr")
    party.partynamechange_set.add(change_second)
    name_second = party.get_name_by_date(date(1995, 1, 1))
    assert name_second.name_short == change_second.name_short


def test_party_family_model(db):
    party_family = PartyFamilyFactory()

    assert str(party_family) == "PartyFamily (1)"
    assert party_family.full_clean() is None
    assert party_family.family.short == "green"


def test_party_family_admin_in_party(admin_client):
    # Django 5.2 adds CSS classes and IDs to inline headings
    response = admin_client.get(reverse("admin:parties_party_add"))
    assert "Party familys" in response.rendered_content
    assert 'id="partyfamily_set-heading"' in response.rendered_content
