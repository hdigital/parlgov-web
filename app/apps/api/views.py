"""Serializers and views for API endpoints."""

from rest_framework import viewsets

from ..data.cabinets.models import Cabinet, CabinetParty
from ..data.core.models import Code, Country
from ..data.elections.models import Election, ElectionResult
from ..data.parties.models import Party, PartyChange, PartyNameChange
from . import serializers


class CountryViewSet(viewsets.ModelViewSet):
    """Rest API view for Country model."""

    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "name_short",
        "name",
    ]


class PartyViewSet(viewsets.ModelViewSet):
    """Rest API view for Party model."""

    queryset = Party.objects.all()
    serializer_class = serializers.PartySerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "name_short",
        "name",
        "name_english",
        "country__name_short",
        "country__name",
    ]


class PartyChangeViewSet(viewsets.ModelViewSet):
    """Rest API view for PartyChange model."""

    queryset = PartyChange.objects.all()
    serializer_class = serializers.PartyChangeSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "date",
        "party__name_short",
        "party__name",
        "party__name_english",
        "party__country__name_short",
        "party__country__name",
    ]


class PartyNameChangeViewSet(viewsets.ModelViewSet):
    """Rest API view for PartyNameChange model."""

    queryset = PartyNameChange.objects.all()
    serializer_class = serializers.PartyNameChangeSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "name_short",
        "name",
        "name_english",
        "date",
        "party__name_short",
        "party__name",
        "party__name_english",
        "party__country__name_short",
        "party__country__name",
    ]


class ElectionViewSet(viewsets.ModelViewSet):
    """Rest API view for Election model."""

    queryset = Election.objects.all()
    serializer_class = serializers.ElectionSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "date",
        "country__name_short",
        "country__name",
    ]


class ElectionResultViewSet(viewsets.ModelViewSet):
    """Rest API view for ElectionResult model."""

    queryset = ElectionResult.objects.all()
    serializer_class = serializers.ElectionResultSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "election__date",
        "election__country__name_short",
        "election__country__name",
        "party__name_short",
        "party__name",
        "party__name_english",
    ]


class CabinetViewSet(viewsets.ModelViewSet):
    """Rest API view for Cabinet model."""

    queryset = Cabinet.objects.all()
    serializer_class = serializers.CabinetSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "name",
        "start_date",
        "country__name_short",
        "country__name",
    ]


class CabinetPartyViewSet(viewsets.ModelViewSet):
    """Rest API view for CabinetParty model."""

    queryset = CabinetParty.objects.all()
    serializer_class = serializers.CabinetPartySerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "cabinet__name",
        "cabinet__start_date",
        "cabinet__country__name_short",
        "cabinet__country__name",
        "party__name_short",
        "party__name",
        "party__name_english",
    ]


class CodeViewSet(viewsets.ModelViewSet):
    """Rest API view for Code model."""

    queryset = Code.objects.all()
    serializer_class = serializers.CodeSerializer
    http_method_names = ["get", "head", "options"]
    search_fields = [
        "table_variable",
        "short",
        "name",
    ]
