"""Create custom django-admin command for './manage.py'.

Run data validation checks.
"""

# ruff: noqa: D103

import datetime

from tqdm import tqdm

import django.apps
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from apps.data.cabinets.models import Cabinet
from apps.data.cabinets.validation import (
    check_cabinet_election,
    check_cabinet_includes_pm,
)
from apps.data.elections.models import Election
from apps.data.elections.validation import (
    check_election_includes_result,
    check_no_seats_party,
    check_one_percent_vote_share,
    check_seats_sum,
    check_vote_share_sum,
)
from apps.data.parties.models import Party
from apps.data.parties.validation import party_include_checks


def validate_all_model_objects() -> None:
    print("\nValidating all models (regular checks) 🔦\n")
    for model in tqdm(django.apps.apps.get_models()):
        for object in model.objects.all():
            try:
                object.full_clean()
            except ValidationError as e:
                print(object, e)


def validate_parties() -> None:  # noqa D103
    print("\n\nValidating parties (extra checks) 🔦\n")
    for party in tqdm(Party.objects.all()):
        party_include_checks(party)


def validate_elections() -> None:  # noqa D103
    print("\n\nValidating elections (extra checks) 🔦\n")
    print("Note — Validation 'no-seats' only for recent elections (since 2010) 📅\n")
    for election in tqdm(Election.objects.all()):
        check_election_includes_result(election)
        if election.date > datetime.date(2010, 1, 1):
            check_no_seats_party(election)
        check_one_percent_vote_share(election)
        check_seats_sum(election)
        check_vote_share_sum(election)


def validate_cabinets() -> None:
    print("\n\nValidating cabinets (extra checks) 🔦\n")
    for cabinet in tqdm(Cabinet.objects.all()):
        check_cabinet_election(cabinet)
        check_cabinet_includes_pm(cabinet)


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "Run all data validation checks"

    def handle(self, *args, **options):
        """Define custom command actions."""
        validate_all_model_objects()
        validate_parties()
        validate_elections()
        validate_cabinets()
