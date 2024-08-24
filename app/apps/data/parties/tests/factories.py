from datetime import date

import factory

from ...core.tests.factories import CodeFactory, CountryFactory

_family_sub_factory = factory.SubFactory(
    CodeFactory,
    table_variable="party_family",
    short="green",
    name="Greens",
)


class PartyFactory(factory.django.DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    family = _family_sub_factory
    name_short = factory.Sequence(lambda n: f"Gru{n+1}")
    name_english = "Greens"
    name = "Die Grünen"
    name_ascii = "Die Gruenen"

    class Meta:
        model = "parties.Party"


class PartyFamilyFactory(factory.django.DjangoModelFactory):
    party = factory.SubFactory(PartyFactory)
    family = _family_sub_factory

    class Meta:
        model = "parties.PartyFamily"


class PartyNameChangeFactory(factory.django.DjangoModelFactory):
    party = factory.SubFactory(PartyFactory)
    date = date(1980, 1, 1)
    name_short = "Gru"
    name_english = "Greens"
    name = "Die Grünen"
    name_ascii = "Die Gruenen"

    class Meta:
        model = "parties.PartyNameChange"


class PartyChangeFactory(factory.django.DjangoModelFactory):
    party = factory.SubFactory(PartyFactory)
    party_new = factory.SubFactory(PartyFactory)
    date = date(1999, 9, 9)
    type = factory.SubFactory(
        CodeFactory,
        table_variable="party_change_type",
        short="successor",
        name="successor",
    )

    class Meta:
        model = "parties.PartyChange"
