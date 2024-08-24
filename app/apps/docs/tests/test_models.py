from django.urls import reverse

from ..models import Page
from .factories import PageFactory


def test_news_model(db, news):
    assert news.type.name == "announcement"
    assert news.title == "Welcome"

    assert str(news) == f"News – {news.date} ({news.id})"


def test_news_admin(admin_client):
    response = admin_client.get(reverse("admin:docs_news_add"))
    assert response.status_code == 200


def test_page_model(db):
    page = PageFactory()

    assert str(page) == f"Page – {page.page} · {page.section} ({page.id})"


def test_page_admin(admin_client):
    response = admin_client.get(reverse("admin:docs_page_add"))
    assert response.status_code == 200


def test_page_get_pages(db):
    page = PageFactory()
    pages = Page.get_by_page(page.page)

    assert pages[page.section] == page
    assert len(pages) == 1
