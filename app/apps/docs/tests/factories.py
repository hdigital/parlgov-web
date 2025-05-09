from datetime import date

from factory import SubFactory
from factory.django import DjangoModelFactory

from ...data.core.tests.factories import CodeFactory


class NewsFactory(DjangoModelFactory):
    date = date(2020, 1, 1)
    type = SubFactory(
        CodeFactory,
        table_variable="news_type",
        short="announce",
        name="announcement",
    )
    title = "Welcome"
    content = "ParlGov is here!"

    class Meta:
        model = "docs.News"


class PageFactory(DjangoModelFactory):
    page = "codebook"
    section = "sources"
    content = "# Data sources"

    class Meta:
        model = "docs.Page"
