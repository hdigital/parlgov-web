import pytest

from django.db.utils import IntegrityError
from django.urls import reverse

from .factories import CabinetPartyFactory


def test_cabinet_party_model(db, cabinet_party):
    id = cabinet_party.id
    assert str(cabinet_party) == f"Cabinet party Deu – 2021 Gru{id} ({id})"

    assert cabinet_party.pm is True


def test_cabinet_party_admin(admin_client):
    response = admin_client.get(reverse("admin:cabinets_cabinetparty_add"))
    assert response.status_code == 200


def test_party_unique(db, cabinet_party):
    with pytest.raises(IntegrityError):
        _ = CabinetPartyFactory(party=cabinet_party.party)


def test_absolute_url(db, cabinet_party):
    assert cabinet_party.get_absolute_url() == "/data/cabinets/deu/2021-07-01/"
