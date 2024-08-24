from django.contrib.staticfiles import finders


def test_bs_css_included():
    absolute_path = finders.find("css/bootstrap.min.css")
    assert absolute_path is not None


def test_bs_css_used(db, client):
    response = client.get("/")
    assert "css/bootstrap.min" in response.rendered_content


def test_bs_js_included():
    absolute_path = finders.find("js/bootstrap.bundle.min.js")
    assert absolute_path is not None


def test_bs_js_used(db, client):
    response = client.get("/")
    assert "js/bootstrap.bundle.min" in response.rendered_content
