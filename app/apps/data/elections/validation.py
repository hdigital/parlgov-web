"""Validation methods for elections data."""

from django.core.exceptions import ValidationError


def check_election_includes_result(election) -> None:
    """Validate election has at least one result.

    Validation is not used in model save to allow adding election models first.
    It is included in 'python manage.py validate_data'
    """
    if not election.electionresult_set.all():
        message = "election must have one result"
        raise ValidationError(message, code="invalid")


def check_election_party_countries(election_result) -> None:
    """Validate country election and party are equal."""
    if election_result.election.country != election_result.party.country:
        message = "election and party countries are not equal"
        raise ValidationError(message, code="invalid")


def check_alliance_no_self_reference(election_result) -> None:
    """Validate alliance -- no self reference (id != alliance_id)."""
    if election_result.id == election_result.alliance.id:
        message = "election result and alliance are equal"
        raise ValidationError(message, code="invalid")


def check_alliance_election_ids_equal(election_result) -> None:
    """Validate alliance -- election equal for result and result alliance."""
    if election_result.election.id != election_result.alliance.election.id:
        message = "election and alliance election are not equal"
        raise ValidationError(message, code="invalid")


def check_no_seats_party(election) -> None:
    """Validate election includes party with no seats (first loser).

    Validation is not used in model save to allow adding election results. It
    is included in 'python manage.py validate_data'
    """
    results = election.electionresult_set.filter(seats=0)

    no_seats = election.data_json.get("no-seats") is False
    no_seats_rule = election.data_json.get("no-seats_rule") is False

    if not results and not (no_seats or no_seats_rule):
        message = f"election without no-seats party (first loser) · '{election}'"
        raise ValidationError(message, code="invalid")


def check_one_percent_vote_share(election) -> None:
    """Validate election with max. one party < 1.0% vote share (no-seats rule).

    Validation is not used in model save to allow adding election results. It
    is included in 'python manage.py validate_data'
    """
    results = election.electionresult_set.filter(seats=0, vote_share__lt=1.0)

    if results.count() >= 2:
        message = f"election with multiple parties < 1% vote share · '{election}'"
        raise ValidationError(message, code="invalid")


def check_seats_sum(election) -> None:
    """Validate election seats sum and seats_total.

    Validation is not used in model save to allow adding election results. It
    is included in 'python manage.py validate_data'
    """
    results = election.electionresult_set.exclude(seats__isnull=True)
    seats_sum = sum([result.seats for result in results if result])

    if seats_sum != election.seats_total:
        message = f"sum of seats and 'seats_total' are not equal · '{election}'"
        raise ValidationError(message, code="invalid")


def check_vote_share_sum(election) -> None:
    """Validate election vote_share sum.

    Validation is not used in model save to allow adding election results. It
    is included in 'python manage.py validate_data'
    """
    if election.data_json.get("vote_share_sum") is True:
        return

    results = election.electionresult_set.exclude(vote_share__isnull=True)
    vote_share_sum = sum([result.vote_share for result in results if result])

    if (vote_share_sum < 85 or vote_share_sum > 101) and vote_share_sum != 0:
        message = f"sum of vote share ({vote_share_sum}) not valid · '{election}'"
        raise ValidationError(message, code="invalid")
