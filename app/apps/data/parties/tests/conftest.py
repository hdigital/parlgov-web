"""Fixtures for tests in 'parties' app."""

import pytest

from .factories import PartyFactory


@pytest.fixture
def party():
    """A 'Party' object with default values."""
    return PartyFactory()
