import pytest

from django.core.exceptions import ValidationError
from django.urls import reverse


def test_country_model(db, country):
    assert str(country) == f"Country – {country.name} ({country.id})"
    assert country.name_short == "DEU"


def test_country_admin(admin_client):
    response = admin_client.get(reverse("admin:datacore_country_add"))
    assert response.status_code == 200


def test_slug_country(db, country):
    assert country.slug == "deu"


def test_iso2_length(db, country):
    country.code_iso2 = "DEU"
    with pytest.raises(ValidationError):
        country.full_clean()


def test_admin_help_country(admin_client):
    response = admin_client.get(reverse("admin:datacore_country_add"))

    assert "observation" in response.rendered_content
