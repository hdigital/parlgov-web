"""Validation methods for cabinet data."""

from django.core.exceptions import ValidationError


def check_cabinet_election(cabinet) -> None:
    """Validate cabinet includes previous election."""
    if cabinet.election != cabinet.get_election():
        message = "cabinet previous election is set incorrectly"
        raise ValidationError(message, code="invalid")


def check_cabinet_includes_pm(cabinet) -> None:
    """Validate cabinet has one PM (except Switzerland).

    Validation is not used in model save to allow adding cabinet parties without
    PMs first and Switzerland data. It is included in 'python manage.py
    validate_data'
    """
    if cabinet.country.name_short == "CHE":
        return

    if not cabinet.cabinetparty_set.filter(pm=True):
        message = "cabinet must have one PM"
        raise ValidationError(message, code="invalid")


def check_cabinet_party_countries(cabinet_party) -> None:
    """Validate country cabinet and party are equal."""
    if cabinet_party.cabinet.country != cabinet_party.party.country:
        message = "cabinet and party countries are not equal"
        raise ValidationError(message, code="invalid")


def check_cabinet_party_no_second_pm(cabinet_party) -> None:
    """Validate cabinet of cabinet party has one PM only."""
    cabinet_pm = cabinet_party.cabinet.cabinetparty_set.filter(pm=True).exclude(
        id=cabinet_party.id
    )
    if cabinet_pm and cabinet_party.pm:
        message = "cabinet can have only one PM"
        raise ValidationError(message, code="invalid")
