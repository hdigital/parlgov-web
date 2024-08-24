from django.urls import reverse


def test_clear_cache_redirect(admin_client):
    response = admin_client.get(reverse("clear_cache"))

    assert response.status_code == 302
    assert response.url == "/"
