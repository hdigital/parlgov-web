"""Create custom django-admin command for './manage.py'.

See 'Command()' for details.
"""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "Create a superuser (development only)"

    def handle(self, *args, **options):
        """Define custom command actions."""
        if not settings.DEBUG:
            raise CommandError("This command is for development purposes only.")

        User = get_user_model()

        username = "django"
        user_exists = User.objects.filter(username=username).exists()

        if not user_exists:
            User.objects.create_superuser(username, "", "this is a django app")
