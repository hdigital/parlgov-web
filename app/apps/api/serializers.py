"""Model serializers for the API app."""

from rest_framework import serializers

from ..data.cabinets.models import Cabinet, CabinetParty
from ..data.core.models import Code, Country
from ..data.elections.models import Election, ElectionResult
from ..data.parties.models import Party, PartyChange, PartyNameChange


class CountrySerializer(serializers.ModelSerializer):
    """Rest API serializer for Country model."""

    class Meta:
        model = Country
        fields = "__all__"


class PartySerializer(serializers.ModelSerializer):
    """Rest API serializer for Party model."""

    class Meta:
        model = Party
        fields = "__all__"


class PartyChangeSerializer(serializers.ModelSerializer):
    """Rest API serializer for PartyChange model."""

    class Meta:
        model = PartyChange
        fields = "__all__"


class PartyNameChangeSerializer(serializers.ModelSerializer):
    """Rest API serializer for PartyNameChange model."""

    class Meta:
        model = PartyNameChange
        fields = "__all__"


class ElectionSerializer(serializers.ModelSerializer):
    """Rest API serializer for Election model."""

    class Meta:
        model = Election
        fields = "__all__"


class ElectionResultSerializer(serializers.ModelSerializer):
    """Rest API serializer for ElectionResult model."""

    class Meta:
        model = ElectionResult
        fields = "__all__"


class CabinetSerializer(serializers.ModelSerializer):
    """Rest API serializer for Cabinet model."""

    class Meta:
        model = Cabinet
        fields = "__all__"


class CabinetPartySerializer(serializers.ModelSerializer):
    """Rest API serializer for CabinetParty model."""

    class Meta:
        model = CabinetParty
        fields = "__all__"


class CodeSerializer(serializers.ModelSerializer):
    """Rest API serializer for Code model."""

    class Meta:
        model = Code
        fields = "__all__"
