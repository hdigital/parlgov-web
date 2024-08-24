from django.urls import reverse


def test_admin_home(client):
    response = client.get("/admin-parlgov/login/?next=/admin/")

    assert response.status_code == 200
    assert "Django" in response.rendered_content


def test_admin_user_login(admin_client):
    response = admin_client.get(reverse("admin:index"))

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == "/admin-parlgov/"
    assert response.context["user"].is_authenticated
