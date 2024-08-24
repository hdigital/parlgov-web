import pytest

from django.urls import reverse

from .views import check_db_table_is_public, fetch_data


@pytest.mark.parametrize(
    "page",
    (
        ("data_party", True),
        ("data_other", False),
        ("view_election", True),
        ("table", False),
    ),
)
def test_public_table(page):
    assert check_db_table_is_public(page[0]) is page[1]


@pytest.mark.django_db
def test_fetch_data():
    assert fetch_data("data_party") is not None
    with pytest.raises(Exception):
        fetch_data("table")


@pytest.mark.django_db
def test_csv_view(client):
    response = client.get(reverse("data_csv", kwargs={"db_table": "data_party"}))

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/csv"


@pytest.mark.django_db
def test_csv_view_table_not_public(client):
    response = client.get(reverse("data_csv", kwargs={"db_table": "django_migrations"}))

    assert response.status_code == 404
