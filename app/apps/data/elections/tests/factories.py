from datetime import date

from factory import SubFactory
from factory.django import DjangoModelFactory

from ...core.tests.factories import CodeFactory, CountryFactory
from ...parties.tests.factories import PartyFactory


class ElectionFactory(DjangoModelFactory):
    type = SubFactory(
        CodeFactory,
        table_variable="election_type",
        short="parliament",
        name="Parliamentary election",
    )
    country = SubFactory(CountryFactory)
    date = date(2020, 1, 1)
    seats_total = 100

    class Meta:
        model = "elections.Election"
        django_get_or_create = ("country", "date")


class ElectionResultFactory(DjangoModelFactory):
    election = SubFactory(ElectionFactory)
    party = SubFactory(PartyFactory)
    seats = 10
    vote_share = 10.0
    votes = 10_000

    class Meta:
        model = "elections.ElectionResult"
