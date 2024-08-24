import pytest

from django.core.exceptions import ValidationError

from ..validators import validate_ascii


def test_ascii_validation():
    validate_ascii("u")

    with pytest.raises(ValidationError):
        validate_ascii("ü")
