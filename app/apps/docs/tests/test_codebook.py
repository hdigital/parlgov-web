import pytest

from ..codebook import codebook_markdown, codebook_pages
from .factories import PageFactory

pytestmark = pytest.mark.django_db


def test_get_codebook_pages():
    pages = codebook_pages()

    assert len(pages) == 5
    assert "codebook" in pages.keys()


def test_create_codebook_markdown():
    _ = PageFactory()

    pages = codebook_pages()
    section = pages["codebook"].first()

    assert section.content == "# Data sources"
    assert "### Data sources" in codebook_markdown()
