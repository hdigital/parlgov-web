"""Validation functions for party data.

See tests for examples of individual checks inclusion criteria.
"""

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db.models import Sum

from ..elections.models import ElectionResult

ALLIANCES_MIN = 2
SEATS_MIN = 2


def check_alliance(party, alliances_min=ALLIANCES_MIN) -> bool:
    """Check if party is an alliances in the minimum number of elections."""
    alliances = ElectionResult.objects.filter(alliance__party=party)
    return alliances.count() >= alliances_min


def check_alliance_member(party, alliances_min=ALLIANCES_MIN) -> bool:
    """Check if party is an alliance member in the minimum number of elections."""
    results = party.electionresult_set
    return results.filter(alliance__isnull=False).count() >= alliances_min


def check_cabinet_party(party) -> bool:
    """Check if party is a cabinet member."""
    return party.cabinetparty_set.exists()


def check_json_include(party) -> bool:
    """Check if party has an include rule specification in 'data_json'."""
    return party.data_json and "include" in party.data_json.keys()


def check_no_party(party) -> bool:
    """Check if party is a 'no party' family entry."""
    return party.family and party.family.short == "none"


def check_seats(party, seats_min=SEATS_MIN) -> bool:
    """Check if party has won the minimum number of seats in a single election."""
    return party.electionresult_set.filter(seats__gte=seats_min).exists()


def check_seats_json(party, seats_min=SEATS_MIN) -> bool:
    """Check if party meets the minimum number of seats in 'data_json'."""
    seats_json = sum(
        [
            result.data_json["seats"]
            for result in party.electionresult_set.all()
            if result.data_json and "seats" in result.data_json.keys()
        ]
    )
    return seats_json >= seats_min


def check_seats_sum(party, seats_min=SEATS_MIN) -> bool:
    """Check if party has won the minimum number of seats in all elections."""
    seats_sum = party.electionresult_set.aggregate(Sum("seats"))["seats__sum"]
    return seats_sum and seats_sum >= seats_min


def check_vote_share(party, vote_share_min=0.95) -> bool:
    """Check if party has the minimum vote share in a single election."""
    if not isinstance(vote_share_min, Decimal):
        vote_share_min = Decimal(str(vote_share_min))

    results = party.electionresult_set
    return results.filter(vote_share__gt=vote_share_min).exists()


def run_include_checks(party) -> str:
    """Run party include checks by order of inclusion criteria.

    Return the first inclusion check that passes.
    """
    checks = (
        check_vote_share,
        check_cabinet_party,
        check_seats,
        check_alliance,
        check_alliance_member,
        check_seats_sum,
        check_seats_json,
        check_no_party,
        # json check last to find redundant entries
        check_json_include,
    )

    for check in checks:
        if check(party):
            return check.__name__.replace("check_", "", 1)

    return ""


def party_include_checks(party) -> None:
    """Validate party inclusion criteria.

    Validation is not used in model save to allow adding parties first. It
    is included in 'python manage.py validate_data'
    """
    if not party.get_include_rule():
        message = f"party inclusion criteria not met · '{party}'"
        raise ValidationError(message, code="invalid")
