"""Utility methods for ParlGov pages."""

from itertools import chain, islice, tee

from django.http import Http404

from .models import Country


def previous_next_item(items_iterable):
    """Get previous and next element of iterable."""
    items_prev, items, items_next = tee(items_iterable, 3)
    items_prev = chain([None], items_prev)
    items_next = chain(islice(items_next, 1, None), [None])
    return zip(items_prev, items, items_next)


def previous_next_object(model_object):
    """Get previous and next object."""
    model = model_object.__class__
    objects = model.objects.all()
    for prev, object, next in previous_next_item(objects):
        if object.id == model_object.id:
            return (prev, next)


def clean_date_format(date_object):
    """Return date string with precision of coding (date, month or year)."""
    if not date_object:
        return ""

    if date_object.month == 7 and date_object.day == 1:
        return date_object.strftime("%Y")
    elif date_object.day == 1:
        return date_object.strftime("%Y-%m")
    else:
        return date_object.strftime("%Y-%m-%d")


def get_country_or_404(country_short):
    """Get country object by short name or raise http 404 error."""
    country = Country.objects.filter(name_short=country_short.upper()).first()

    if not country:
        raise Http404

    return country
