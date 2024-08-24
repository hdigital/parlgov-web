"""Template tags to format data."""

import re
from datetime import date

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def ymd_remove_07_01(date_format: date) -> str:
    """Format date as 'Y-m-d' but remove '-07-01' (see codebook)."""
    if not isinstance(date_format, date):
        return date_format

    return date_format.strftime("%Y-%m-%d").replace("-07-01", "")


@register.filter
def round_100(value: int) -> int:
    """Round number to nearest hundred."""
    return round(value / 100.0) * 100


@register.filter()
@stringfilter
def wikipedia_title(wp_url: str) -> str:
    """Extract title from Wikipedia url."""
    if wp_url.find("wikipedia") == -1:
        return wp_url

    entry = wp_url.split("/")[-1].replace("_", " ")
    entry = re.sub("(%..)+", "·", entry)

    return entry
