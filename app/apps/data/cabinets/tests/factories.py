from datetime import date

import factory

from ...core.tests.factories import CountryFactory
from ...parties.tests.factories import PartyFactory


class CabinetFactory(factory.django.DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    name = "Bundeskanzler"
    start_date = date(2021, 7, 1)

    class Meta:
        model = "cabinets.Cabinet"
        django_get_or_create = ("country", "start_date")


class CabinetPartyFactory(factory.django.DjangoModelFactory):
    cabinet = factory.SubFactory(CabinetFactory)
    party = factory.SubFactory(PartyFactory)
    pm = True

    class Meta:
        model = "cabinets.CabinetParty"
