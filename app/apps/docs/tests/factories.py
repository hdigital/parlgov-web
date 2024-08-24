from datetime import date

import factory

from ...data.core.tests.factories import CodeFactory


class NewsFactory(factory.django.DjangoModelFactory):
    date = date(2020, 1, 1)
    type = factory.SubFactory(
        CodeFactory,
        table_variable="news_type",
        short="announce",
        name="announcement",
    )
    title = "Welcome"
    content = "ParlGov is here!"

    class Meta:
        model = "docs.News"


class PageFactory(factory.django.DjangoModelFactory):
    page = "codebook"
    section = "sources"
    content = "# Data sources"

    class Meta:
        model = "docs.Page"
