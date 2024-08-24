import pytest

from django.core.exceptions import ValidationError
from django.urls import reverse

from .factories import CodeFactory


@pytest.fixture
def code():
    """A 'Code' object with default values."""
    return CodeFactory()


def test_code_model(db, code):
    code.full_clean()
    assert str(code) == f"Code – {code.short} ({code.id})"
    assert code.short == "update"


def test_code_admin(admin_client):
    response = admin_client.get(reverse("admin:datacore_code_add"))
    assert response.status_code == 200


def test_table_defined(db, code):
    code.table_variable = "undefined"
    with pytest.raises(ValidationError):
        code.full_clean()


def test_short_name_unique(db, code):
    code_two = CodeFactory(short="new")
    with pytest.raises(ValidationError):
        code_two.short = code.short
        code_two.full_clean()
