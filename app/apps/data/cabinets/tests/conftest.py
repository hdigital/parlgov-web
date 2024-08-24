"""Fixtures for tests in 'cabinets' app."""

import pytest

from ...elections.tests.factories import ElectionFactory
from ...parties.tests.factories import PartyFactory
from .factories import CabinetFactory, CabinetPartyFactory


@pytest.fixture
def cabinet():
    """A 'Cabinet' object with default values."""
    return CabinetFactory()


@pytest.fixture
def cabinet_party():
    """A 'CabinetParty' object with default values.

    Resets the party 'name_short' factory sequence for each test.
    """
    PartyFactory.reset_sequence()

    return CabinetPartyFactory()


@pytest.fixture
def cabinet_election(cabinet):
    """An 'Election' object for a cabinet.

    Election date is the same as the cabinet's start date.
    """
    return ElectionFactory(country=cabinet.country, date=cabinet.start_date)
