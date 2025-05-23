from factory.django import DjangoModelFactory


class CodeFactory(DjangoModelFactory):
    table_variable = "news_type"
    order = 100
    short = "update"
    name = "update code"

    class Meta:
        model = "datacore.Code"
        django_get_or_create = ("short",)


class CountryFactory(DjangoModelFactory):
    name = "Germany"
    name_short = "DEU"
    code_iso2 = "DE"

    class Meta:
        model = "datacore.Country"
        django_get_or_create = ("name_short",)
