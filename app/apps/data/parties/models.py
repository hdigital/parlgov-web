from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from ...base.models import (
    BaseModel,
    comment_help_text,
    data_json_help_text,
    description_help_text,
)
from ..core import helptext
from ..core.utils import clean_date_format
from ..core.validators import validate_ascii, validate_no_space
from .validation import run_include_checks


class Party(BaseModel):
    """Party information."""

    country = models.ForeignKey("datacore.Country", on_delete=models.PROTECT)
    family = models.ForeignKey(
        "datacore.Code",
        db_column="family_id",
        limit_choices_to={"table_variable": "party_family", "order__lt": 200},
        on_delete=models.PROTECT,
    )
    name_short = models.CharField(
        db_index=True, max_length=10, validators=[validate_ascii, validate_no_space]
    )
    name_english = models.CharField(
        db_index=True, max_length=200, validators=[validate_ascii]
    )
    name = models.CharField(db_index=True, max_length=200)
    name_ascii = models.CharField(
        db_index=True, max_length=200, validators=[validate_ascii]
    )
    name_nonlatin = models.CharField(blank=True, max_length=200)
    wikipedia = models.URLField(null=True, blank=True, max_length=200)
    foundation_date = models.DateField(
        null=True, blank=True, help_text=helptext.date_help_text
    )
    dissolution_date = models.DateField(null=True, blank=True)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=helptext.data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    def get_absolute_url(self):
        """Get url for party object."""
        url_parameters = {"country": self.country.slug, "party_id": self.id}
        return reverse("parties:detail", kwargs=url_parameters)

    def get_include_rule(self):
        """Get inclusion criteria for party based on codebook rules."""
        return run_include_checks(self)

    def get_name_by_date(self, date):
        """Get party name by date from PartyNameChange or Party model."""
        parties = self.partynamechange_set.filter(date__lte=date)

        if parties:
            return parties.last()
        else:
            return self

    class Meta:
        db_table = "data_party"
        ordering = ("country", "name_ascii")
        constraints = [
            models.UniqueConstraint(
                fields=["country", "name_short"],
                name="unique_party_name_short_per_country",
            ),
        ]

    def __str__(self):
        country = self.country.name_short.capitalize()
        return f"Party {country} — {self.name_short} ({self.id})"


class PartyFamily(BaseModel):
    """Additional party families (esp. for 'special issue' parties)."""

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    family = models.ForeignKey(
        "datacore.Code",
        db_column="type_id",
        limit_choices_to={"table_variable": "party_family"},
        on_delete=models.PROTECT,
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    class Meta:
        db_table = "data_party_family"

    def __str__(self):
        return f"PartyFamily ({self.id})"


class PartyNameChange(BaseModel):
    """All name changes of a party with date."""

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    date = models.DateField(help_text=helptext.date_help_text)
    party_change = models.BooleanField(default=False)
    name_short = models.CharField(
        blank=True, max_length=10, validators=[validate_ascii]
    )
    name_english = models.CharField(
        blank=True, max_length=200, validators=[validate_ascii]
    )
    name = models.CharField(blank=True, max_length=200)
    name_ascii = models.CharField(
        blank=True, max_length=200, validators=[validate_ascii]
    )
    name_nonlatin = models.CharField(blank=True, max_length=200)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=helptext.data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    @property
    def date_clean(self):
        """Date by precision of coding."""
        return clean_date_format(self.date)

    @property
    def family(self):
        """Shortcut party family object."""
        return self.party.family

    class Meta:
        db_table = "data_party_name_change"
        ordering = (
            "party",
            "date",
        )

    def __str__(self):
        country = self.party.country.name_short.capitalize()
        return f"PartyNameChange {country} — {self.party.name_short} ({self.id})"


class PartyChange(BaseModel):
    """Party changes linking predecessor and successor party."""

    party = models.ForeignKey(
        Party, related_name="partychange_set", on_delete=models.CASCADE
    )
    party_new = models.ForeignKey(
        Party,
        db_column="party_id_new",
        related_name="partychange_new_set",
        on_delete=models.CASCADE,
    )
    date = models.DateField(db_index=True, help_text=helptext.date_help_text)
    type = models.ForeignKey(
        "datacore.Code",
        db_column="type_id",
        null=True,
        blank=True,
        limit_choices_to={"table_variable": "party_change_type"},
        on_delete=models.CASCADE,
    )
    data_source = models.CharField(
        blank=True, max_length=200, help_text=helptext.data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    @property
    def date_clean(self):
        """Return date format with precision (e.g. '2010-07-01' as '2010')."""
        return clean_date_format(self.date)

    def clean(self):
        """Check that countries of party change are equal."""
        if self.party.country != self.party_new.country:
            raise ValidationError("countries are not equal", code="invalid")
        return super().clean()  # pragma: no cover

    class Meta:
        db_table = "data_party_change"
        ordering = ("date",)
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(party=models.F("party_new")),
                name="party_and_party_new_not_equal",
            ),
        ]

    def __str__(self):
        country = self.party.country.name_short.capitalize()
        return (
            f"PartyChange {country} — {self.party.name_short} // "
            f"{self.party_new.name_short} ({self.id})"
        )
