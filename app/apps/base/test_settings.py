import pytest

from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.test import override_settings

from apps.data.parties.tests.factories import PartyFactory


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


@pytest.mark.django_db
@override_settings(
    CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
)
def test_cache_middleware_varies_on_cookie(client, admin_user):
    """Cached pages are not shared between visitors and logged-in users."""
    cache.clear()
    party = PartyFactory(comment="editor comment")
    url = party.get_absolute_url()

    response = client.get(url)
    assert "editor comment" not in response.rendered_content
    assert "Cookie" in response["Vary"]

    client.force_login(admin_user)
    response = client.get(url)
    assert "editor comment" in response.content.decode()

    client.logout()
    response = client.get(url)
    assert "editor comment" not in response.content.decode()
