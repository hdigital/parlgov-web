from datetime import date

import pytest

from django.http import Http404

from ..utils import (
    clean_date_format,
    get_country_or_404,
    previous_next_item,
    previous_next_object,
)


def test_prev_next_iterable():
    items = [1, 2]
    items_prev_next = list(previous_next_item(items))

    assert items_prev_next[0] == (None, 1, 2)
    assert items_prev_next[1] == (1, 2, None)


def test_prev_next_object(db, django_user_model):
    object_a = django_user_model.objects.create(username="a")
    object_b = django_user_model.objects.create(username="b")

    assert previous_next_object(object_a)[1] == object_b
    assert previous_next_object(object_b)[0] == object_a


def test_clean_date():
    assert clean_date_format(None) == ""
    assert clean_date_format(date(2020, 7, 1)) == "2020"
    assert clean_date_format(date(2020, 2, 1)) == "2020-02"
    assert clean_date_format(date(2020, 2, 2)) == "2020-02-02"


def test_get_country_or_404(db, country):
    country_get = get_country_or_404("DEU")
    assert country_get.name == "Germany"

    with pytest.raises(Http404):
        get_country_or_404("DDD")
