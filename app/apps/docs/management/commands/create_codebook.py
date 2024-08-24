"""Create custom django-admin command for './manage.py'.

Create codebook in Markdown format.
"""

# ruff: noqa: D103

from django.core.management.base import BaseCommand

from ...codebook import codebook_markdown


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "Create codebook in Markdown format"

    def handle(self, *args, **options):
        """Create codebook in Markdown format."""
        return codebook_markdown()
