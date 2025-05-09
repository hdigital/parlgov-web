from datetime import date

from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from ...core.tests.factories import CodeFactory, CountryFactory

_family_sub_factory = SubFactory(
    CodeFactory,
    table_variable="party_family",
    short="green",
    name="Greens",
)


class PartyFactory(DjangoModelFactory):
    country = SubFactory(CountryFactory)
    family = _family_sub_factory
    name_short = Sequence(lambda n: f"Gru{n+1}")
    name_english = "Greens"
    name = "Die Grünen"
    name_ascii = "Die Gruenen"

    class Meta:
        model = "parties.Party"


class PartyFamilyFactory(DjangoModelFactory):
    party = SubFactory(PartyFactory)
    family = _family_sub_factory

    class Meta:
        model = "parties.PartyFamily"


class PartyNameChangeFactory(DjangoModelFactory):
    party = SubFactory(PartyFactory)
    date = date(1980, 1, 1)
    name_short = "Gru"
    name_english = "Greens"
    name = "Die Grünen"
    name_ascii = "Die Gruenen"

    class Meta:
        model = "parties.PartyNameChange"


class PartyChangeFactory(DjangoModelFactory):
    party = SubFactory(PartyFactory)
    party_new = SubFactory(PartyFactory)
    date = date(1999, 9, 9)
    type = SubFactory(
        CodeFactory,
        table_variable="party_change_type",
        short="successor",
        name="successor",
    )

    class Meta:
        model = "parties.PartyChange"
