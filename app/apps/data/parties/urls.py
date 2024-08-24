from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "parties"

urlpatterns = [
    path(
        "<slug:country>/<int:party_id>/",
        views.party_detail_view,
        name="detail",
    ),
    path(
        "<slug:country>/",
        views.party_list_view,
        name="list",
    ),
    path(
        "",
        RedirectView.as_view(pattern_name="country_list"),
        name="index_redirect",
    ),
]
