from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from ..core.utils import get_country_or_404, previous_next_object
from .models import Election, ElectionResult


def election_detail_view(request, country: str, election_date: str, ep: bool = False):
    """Details of elections page (parliament and EP)."""
    election = get_object_or_404(
        Election,
        country__name_short=country.upper(),
        date=election_date,
        type__short="parliament" if not ep else "ep",
    )

    if election.type.short == "ep":
        election.ep_previous_election = Election.get_by_date(
            election.country, election.date
        )

    results = (
        ElectionResult.objects.filter(election=election, alliance__isnull=True)
        .prefetch_related(
            "alliance_set", "alliance_set__election", "alliance_set__party__country"
        )
        .select_related("alliance__party", "election", "party__country")
    )

    cabinets = election.cabinet_set.select_related("country")

    context = {
        "election": election,
        "election_results": results,
        "cabinets": cabinets,
        "previous_next": previous_next_object(election),
    }

    return TemplateResponse(request, "data/election-detail.html", context)


def election_list_view(request, country: str):
    """List elections filtered by country short."""
    context = {"country": get_country_or_404(country)}
    context["election_list"] = (
        Election.objects.select_related("country", "type")
        .prefetch_related("electionresult_set__party__country")
        .filter(country=context["country"])
        .order_by("type", "-date")
    )

    return TemplateResponse(request, "data/election-list.html", context)
