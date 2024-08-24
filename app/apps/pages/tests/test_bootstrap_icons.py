from django.contrib.staticfiles import finders


def test_bs_icons_included():
    paths = (
        "css/bootstrap-icons.css",
        "css/fonts/bootstrap-icons.woff",
        "css/fonts/bootstrap-icons.woff2",
    )
    for path in paths:
        assert finders.find(path) is not None


def test_bs_icons_used(db, client):
    response = client.get("/")
    assert "css/bootstrap-icons" in response.rendered_content
    assert "bi-table" in response.rendered_content
