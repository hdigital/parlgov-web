"""URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .base import views as views_base
from .data.core import views as views_core
from .views_data import views as views_data

urlpatterns = [
    # Data urls
    path("data/parties/", include("apps.data.parties.urls")),
    path("data/elections/", include("apps.data.elections.urls")),
    path("data/cabinets/", include("apps.data.cabinets.urls")),
    path("data/", views_core.data_index_view, name="country_list"),
    # CSV tables
    path("data-csv/<slug:db_table>/", views_data.csv_view, name="data_csv"),
    # Documentation urls
    path("docs/", include("apps.docs.urls")),
    # API urls
    path("api/", include("apps.api.urls")),
    # path("api-auth/", include("rest_framework.urls")),
    # Page urls
    path("", include("apps.pages.urls")),
    # Misc urls
    path("clear-cache", views_base.clear_cache, name="clear_cache"),
    # Admin urls
    path("admin-parlgov/doc/", include("django.contrib.admindocs.urls")),
    path("admin-parlgov/", admin.site.urls),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
