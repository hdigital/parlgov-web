from django.db import models

from ...base.models import (
    BaseModel,
    comment_help_text,
    data_json_help_text,
    description_help_text,
)

CODE_CHOICES = (
    ("party_family", "party — family_id"),
    ("party_change_type", "party change — type_id"),
    ("election_type", "election — type_id"),
    ("election_ep_type", "election ep — type_id"),
    ("cabinet_termination", "cabinet — termination_id"),
    ("cabinet_support", "cabinet_support — type_id"),
    ("confidence_vote", "confidence_vote — type_id"),
    ("news_type", "news — type_id"),
)


class Code(BaseModel):
    """Codes for categories of variables in models (e.g. party_family)."""

    table_variable = models.CharField(
        db_index=True, max_length=100, choices=CODE_CHOICES
    )
    order = models.PositiveIntegerField(db_index=True)
    short = models.SlugField(db_index=True, max_length=25)
    name = models.CharField(max_length=50)
    wikipedia = models.URLField(blank=True, max_length=200)
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    class Meta:
        db_table = "data_code"
        ordering = ("table_variable", "order")
        constraints = [
            models.UniqueConstraint(
                fields=["table_variable", "short"], name="unique_short_name_per_table"
            ),
        ]

    def __str__(self):
        return f"Code – {self.short} ({self.id})"


class Country(BaseModel):
    """Countries covered in ParlGov."""

    name = models.CharField(max_length=100, unique=True)
    name_short = models.CharField(db_index=True, max_length=3, unique=True)
    flag = models.CharField(max_length=2)
    code_iso2 = models.CharField(max_length=2, unique=True)
    eu_accession_date = models.DateField(null=True, blank=True)
    oecd_accession_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    @property
    def slug(self):
        """Get country short lower case."""
        return self.name_short.lower()

    class Meta:
        db_table = "data_country"
        ordering = ("name",)

    def __str__(self):
        return f"Country – {self.name} ({self.id})"
