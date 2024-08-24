from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "elections"

urlpatterns = [
    path(
        "<slug:country>/<slug:election_date>-ep/",
        views.election_detail_view,
        kwargs={"ep": True},
        name="detail_ep",
    ),
    path(
        "<slug:country>/<slug:election_date>/",
        views.election_detail_view,
        name="detail",
    ),
    path(
        "<slug:country>/",
        views.election_list_view,
        name="list",
    ),
    path(
        "",
        RedirectView.as_view(pattern_name="country_list"),
        name="index_redirect",
    ),
]
