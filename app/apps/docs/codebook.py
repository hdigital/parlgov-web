"""Create codebook from database entries."""

from datetime import datetime

from django.template.loader import render_to_string

from .models import Page


def codebook_pages() -> dict:
    """Get all codebook pages from database."""
    pages = {"today": datetime.now()}

    for page in ["changelog", "codebook", "country", "credits"]:
        pages[page] = Page.objects.filter(page=page)

    return pages


def codebook_markdown() -> str:
    """Create codebook text in Markdown format."""
    context = codebook_pages()

    return render_to_string("docs/codebook-markdown.txt", context)
