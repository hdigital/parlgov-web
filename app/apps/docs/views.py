from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import generic

from .codebook import codebook_markdown, codebook_pages
from .models import News


def codebook_view(request):
    """Create codebook page."""
    context = codebook_pages()

    return TemplateResponse(request, "docs/codebook.html", context)


def codebook_markdown_view(request):
    """Create Markdown codebook page."""
    return HttpResponse(
        content=codebook_markdown(),
        content_type="text/plain; charset=utf-8",
    )


class NewsListView(generic.ListView):
    model = News
    template_name = "docs/news.html"
