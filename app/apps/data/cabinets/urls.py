from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "cabinets"

urlpatterns = [
    path(
        "<slug:country>/<slug:cabinet_date>/",
        views.cabinet_detail_view,
        name="detail",
    ),
    path(
        "<slug:country>/",
        views.cabinet_list_view,
        name="list",
    ),
    path(
        "",
        RedirectView.as_view(pattern_name="country_list"),
        name="index_redirect",
    ),
]
