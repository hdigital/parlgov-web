from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register(r"countries", views.CountryViewSet)
router.register(r"parties", views.PartyViewSet)
router.register(r"party-name-changes", views.PartyNameChangeViewSet)
router.register(r"party-changes", views.PartyChangeViewSet)
router.register(r"elections", views.ElectionViewSet)
router.register(r"election-results", views.ElectionResultViewSet)
router.register(r"cabinets", views.CabinetViewSet)
router.register(r"cabinet-parties", views.CabinetPartyViewSet)
router.register(r"codes", views.CodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
