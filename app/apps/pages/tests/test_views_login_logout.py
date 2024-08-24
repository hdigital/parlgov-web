import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_settings_login_logout_redirect_urls():
    from config.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL

    assert LOGIN_REDIRECT_URL is not None
    assert LOGOUT_REDIRECT_URL is not None


def test_login(client):
    response = client.get(reverse("page:login"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/login-parlgov"
    assert "Login" in response.rendered_content

    assertTemplateUsed(response, "pages/login.html")


def test_logout(logged_in_client):
    response = logged_in_client.get(reverse("page:home"))

    assert "bi-box" in response.rendered_content
