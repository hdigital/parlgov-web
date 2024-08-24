"""Define project validators for Django models."""

from django.core.exceptions import ValidationError


def validate_ascii(value):
    """Check if all characters are ascii values."""
    if not value.isascii():
        raise ValidationError(f"'{value}' is not valid ascii", code="invalid")


def validate_no_space(value):
    """Check that no space is in string value."""
    if " " in value:
        raise ValidationError(f"'{value}' includes space", code="invalid")
