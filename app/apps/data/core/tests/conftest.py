"""Fixtures for tests in 'data.core' app."""

import pytest

from .factories import CountryFactory


@pytest.fixture
def country():
    """A 'Country' object with default values."""
    return CountryFactory()
