"""Pytest configuration of app fixtures."""

import pytest


@pytest.fixture
def logged_in_client(client, django_user_model):
    """A Django test client logged in as a user.

    Used in tests that need access to log-in protected pages and sections.
    """
    user = django_user_model.objects.create_user(username="user", password="password")
    client.force_login(user)

    return client
