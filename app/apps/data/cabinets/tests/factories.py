from datetime import date

from factory import SubFactory
from factory.django import DjangoModelFactory

from ...core.tests.factories import CountryFactory
from ...parties.tests.factories import PartyFactory


class CabinetFactory(DjangoModelFactory):
    country = SubFactory(CountryFactory)
    name = "Bundeskanzler"
    start_date = date(2021, 7, 1)

    class Meta:
        model = "cabinets.Cabinet"
        django_get_or_create = ("country", "start_date")


class CabinetPartyFactory(DjangoModelFactory):
    cabinet = SubFactory(CabinetFactory)
    party = SubFactory(PartyFactory)
    pm = True

    class Meta:
        model = "cabinets.CabinetParty"
