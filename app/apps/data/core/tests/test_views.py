import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_country_list(client, country):
    response = client.get(reverse("country_list"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/data/"

    assert "Germany" in response.rendered_content
    assert '<div class="col-sm-3">' in response.rendered_content

    assertTemplateUsed(response, "data/data-index.html")
