from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from ..core.utils import get_country_or_404, previous_next_object
from .models import Party


def party_detail_view(request, country: str, party_id: int):
    """Create party detail page."""
    party = get_object_or_404(
        Party.objects.prefetch_related(
            "partychange_set__party__country",
            "partychange_new_set__party__country",
        ),
        id=party_id,
        country__name_short=country.upper(),
    )
    elections = party.electionresult_set.select_related(
        "election__country", "election__type"
    )
    cabinets = party.cabinetparty_set.select_related("cabinet__country")

    context = {
        "party": party,
        "elections": elections.filter(election__type__short="parliament"),
        "elections_ep": elections.filter(election__type__short="ep"),
        "cabinets": cabinets,
        "previous_next": previous_next_object(party),
    }

    return TemplateResponse(request, "data/party-detail.html", context)


def party_list_view(request, country: str):
    """List parties filtered by country short."""
    country = get_country_or_404(country)
    parties = (
        Party.objects.annotate(Count("electionresult", distinct=True))
        .annotate(Count("cabinetparty", distinct=True))
        .prefetch_related("partynamechange_set__party")
        .select_related("country")
        .filter(country=country)
        .order_by("name_ascii")
    )

    context = {"country": country, "party_list": parties}

    return TemplateResponse(request, "data/party-list.html", context)
