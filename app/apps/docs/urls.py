from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "docs"

urlpatterns = [
    path(
        "codebook/",
        views.codebook_view,
        name="codebook",
    ),
    path(
        "codebook-markdown/",
        views.codebook_markdown_view,
        name="codebook_markdown",
    ),
    path(
        "news/",
        views.NewsListView.as_view(),
        name="news",
    ),
    path(
        "",
        RedirectView.as_view(pattern_name="docs:codebook"),
        name="index",
    ),
]
