"""Create custom django-admin command for './manage.py'.

See 'Command()' for details.
"""

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from apps.data.elections.models import Election
from apps.data.elections.validation import check_no_seats_party


def validate_no_seats() -> None:
    """List all elections that do not have a party with no seats."""
    for election in Election.objects.all():
        try:
            check_no_seats_party(election)
        except ValidationError as e:
            print(f"Validation error: {e}")


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "List elections that do not have a party with no seat."

    def handle(self, *args, **options):
        """Define custom command actions."""
        validate_no_seats()
