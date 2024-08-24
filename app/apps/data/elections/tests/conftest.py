"""Fixtures for tests in 'elections' app."""

import pytest

from ...core.tests.factories import CodeFactory
from ...parties.tests.factories import PartyFactory
from .factories import ElectionFactory, ElectionResultFactory


@pytest.fixture
def election():
    """An 'Election' object with default values."""
    return ElectionFactory()


@pytest.fixture
def election_ep():
    """An European election object with default election values."""
    return ElectionFactory(type=CodeFactory(short="ep"))


@pytest.fixture
def election_result():
    """An 'ElectionResult' object with default values.

    Resets the party 'name_short' factory sequence for each test.
    """
    PartyFactory.reset_sequence()

    return ElectionResultFactory()
