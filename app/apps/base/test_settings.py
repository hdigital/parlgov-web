import pytest

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def test_password_valid():
    assert validate_password("123456789012345x") is None


def test_password_minimal_length():
    with pytest.raises(ValidationError) as error:
        validate_password("123456789012345")

    assert "too short" in " ".join(error.value.messages)


def test_password_not_numeric():
    with pytest.raises(ValidationError) as error:
        validate_password("12345678901234567")

    assert "entirely numeric" in " ".join(error.value.messages)
