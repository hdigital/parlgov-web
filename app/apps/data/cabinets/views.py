from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from ..core.utils import get_country_or_404, previous_next_object
from .models import Cabinet, CabinetParty


def cabinet_detail_view(request, country: str, cabinet_date: str):
    """Details of cabinet page."""
    cabinet = get_object_or_404(
        Cabinet, country__name_short=country.upper(), start_date=cabinet_date
    )
    parties = CabinetParty.objects.filter(cabinet=cabinet).select_related(
        "party__country"
    )

    context = {
        "cabinet": cabinet,
        "parties": parties,
        "previous_next": previous_next_object(cabinet),
    }

    return TemplateResponse(request, "data/cabinet-detail.html", context)


def cabinet_list_view(request, country: str):
    """List cabinets filtered by country short."""
    context = {"country": get_country_or_404(country)}
    context["cabinet_list"] = (
        Cabinet.objects.select_related("country")
        .prefetch_related("cabinetparty_set__party__country")
        .filter(country=context["country"])
        .order_by("-start_date")
    )

    return TemplateResponse(request, "data/cabinet-list.html", context)
