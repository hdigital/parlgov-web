from datetime import date, timedelta

import pytest

from django.core.exceptions import ValidationError
from django.db import connection
from django.db.utils import IntegrityError
from django.urls import reverse

from ..models import Cabinet
from .factories import CabinetFactory


def test_cabinet_model(db, cabinet):
    assert str(cabinet) == "Cabinet Deu – 2021 Bundeskanzler (1)"

    assert cabinet.start_date == date(2021, 7, 1)


def test_cabinet_admin(admin_client):
    response = admin_client.get(reverse("admin:cabinets_cabinet_add"))
    assert response.status_code == 200


def test_cabinet_election(db, cabinet, cabinet_election):
    cabinet.save()  # update 'cabinet.election' on save

    assert cabinet.election == cabinet_election


def test_cabinet_election_update(db, cabinet, cabinet_election):
    """Test that an external change of 'cabinet.election' is updated on save."""
    cabinet.save()  # update 'cabinet.election' on save

    # change value of 'cabinet.election' externally with SQL
    cursor = connection.cursor()
    cursor.execute(
        f"""UPDATE data_cabinet
            SET election_id = NULL
            WHERE id = {cabinet.id};"""
    )

    cabinet_get = Cabinet.objects.get(id=cabinet.id)
    assert cabinet_get.election != cabinet_get.get_election()

    cabinet_get.save()  # update 'cabinet.election' on save
    assert cabinet_get.election == cabinet_get.get_election()
    assert cabinet_get.election == cabinet_election


def test_name_ascii(db, cabinet):
    cabinet.name = "ÄÖÜ"
    with pytest.raises(ValidationError):
        cabinet.full_clean()


def test_name_unique(db, cabinet):
    with pytest.raises(IntegrityError):
        CabinetFactory(name=cabinet.name, start_date="1999-09-09")


def test_date_unique(db, cabinet):
    cabinet_two = CabinetFactory(name="Second Cabinet", start_date="1999-09-09")
    cabinet_two.start_date = cabinet.start_date

    with pytest.raises(ValidationError):
        cabinet_two.full_clean()


def test_date_start_not_equal_termination(db, cabinet):
    cabinet.termination_date = cabinet.start_date
    cabinet.save()  # equal dates don't raise exception


def test_date_start_not_smaller_than_termination(db, cabinet):
    cabinet.termination_date = cabinet.start_date - timedelta(days=1)
    with pytest.raises(IntegrityError):
        cabinet.save()


def test_absolute_url(db, cabinet):
    assert cabinet.get_absolute_url() == "/data/cabinets/deu/2021-07-01/"
