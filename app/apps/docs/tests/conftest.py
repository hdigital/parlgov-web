"""Fixtures for tests in 'cabinets' app."""

import pytest

from .factories import NewsFactory


@pytest.fixture
def news():
    """A 'News' object with default values."""
    return NewsFactory()
