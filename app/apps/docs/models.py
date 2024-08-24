from django.db import models

from ..base.models import BaseModel, data_json_help_text, markdown_help_text


class News(BaseModel):
    """News announcements of project history."""

    date = models.DateField()
    author = models.CharField(
        blank=True,
        max_length=100,
        help_text="lowercase initials of author(s) name(s) (e.g. 'hd/pm')",
    )
    title = models.CharField(max_length=100)
    content = models.TextField(help_text=markdown_help_text)
    country = models.ForeignKey(
        "datacore.Country", on_delete=models.PROTECT, null=True, blank=True
    )
    type = models.ForeignKey(
        "datacore.Code",
        on_delete=models.PROTECT,
        limit_choices_to={"table_variable": "news_type"},
    )

    class Meta:
        db_table = "docs_news"
        ordering = ("-date", "-id")
        verbose_name_plural = "news"

    def __str__(self):
        return f"News – {self.date} ({self.id})"


class Page(BaseModel):
    """Documentation pages (codebook, changelog, etc.)."""

    page = models.SlugField(db_index=True)
    section = models.SlugField(blank=True, db_index=True)
    content = models.TextField()
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    @classmethod
    def get_by_page(cls, page):
        """Get all sections of a page."""
        pages = cls.objects.filter(page=page)
        pages = {page.section: page for page in pages}
        return pages if pages else None

    class Meta:
        db_table = "docs_page"
        ordering = (
            "page",
            "section",
        )
        unique_together = ("page", "section")

    def __str__(self):
        return f"Page – {self.page} · {self.section} ({self.id})"
