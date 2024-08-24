"""Create custom django-admin command for './manage.py'.

Update cabinet election for all cabinets.

A Cabinet's election is added and updated on save for a 'Cabinet' object.
An election may be removed or it's date may be changed. Such a change to
an 'Election' object is not automatically updated in 'Cabinet' objects.
"""

from tqdm import tqdm

from django.core.management.base import BaseCommand

from apps.data.cabinets.models import Cabinet


def update_cabinet_election() -> None:
    """Update cabinet election if value is not up-to-date."""
    print("\nChecking elections of cabinets  🔦\n")
    for cabinet in tqdm(Cabinet.objects.all()):
        if cabinet.election != cabinet.get_election():
            print(f"Updating election for {cabinet}")
            cabinet.save()


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "Check and update cabinet election"

    def handle(self, *args, **options):
        """Define custom command actions."""
        update_cabinet_election()
