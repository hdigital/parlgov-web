from django.db import models
from django.urls import reverse

from ...base.models import (
    BaseModel,
    comment_help_text,
    data_json_help_text,
    description_help_text,
)
from ..core.helptext import data_source_help_text
from ..core.validators import validate_ascii
from ..elections.models import Election
from . import validation


class Cabinet(BaseModel):
    """Cabinet information."""

    country = models.ForeignKey("datacore.Country", on_delete=models.PROTECT)
    name = models.CharField(db_index=True, max_length=50, validators=[validate_ascii])
    start_date = models.DateField(db_index=True)
    termination_date = models.DateField(null=True, blank=True)
    caretaker = models.BooleanField(default=False)
    election = models.ForeignKey(
        "elections.Election",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="previous election — value is added or updated on save",
    )
    wikipedia = models.URLField(null=True, blank=True, max_length=200)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    def get_election(self):
        """Get the previous election.

        The method is used in 'self.save()' to set the 'self.election' attribute.
        """
        return Election.get_by_date(self.country, self.start_date)

    def get_absolute_url(self):
        """Get url for cabinet object)."""
        url_parameters = {"country": self.country.slug, "cabinet_date": self.start_date}
        return reverse("cabinets:detail", kwargs=url_parameters)

    def save(self, *args, **kwargs):
        """Save cabinet model and set values."""
        if self.election != self.get_election():
            self.election = self.get_election()

        super().save(*args, **kwargs)

    class Meta:
        db_table = "data_cabinet"
        ordering = ("country", "start_date")
        constraints = [
            models.UniqueConstraint(
                fields=["country", "name"],
                name="unique_cabinet_name_per_country",
            ),
            models.UniqueConstraint(
                fields=["country", "start_date"],
                name="unique_cabinet_date_per_country",
            ),
            models.CheckConstraint(
                check=models.Q(start_date__lte=models.F("termination_date")),
                name="cabinet_start_date_smaller_than_termination_date",
            ),
        ]

    def __str__(self):
        country = self.country.name_short.capitalize()
        return f"Cabinet {country} – {self.start_date.year} {self.name} ({self.id})"


class CabinetParty(BaseModel):
    """Cabinet membership of party."""

    cabinet = models.ForeignKey(
        Cabinet,
        on_delete=models.CASCADE,
    )
    party = models.ForeignKey(
        "parties.Party",
        on_delete=models.PROTECT,
    )
    pm = models.BooleanField(default=False)
    defector = models.BooleanField(
        default=False,
        help_text=(
            "Add information in description field why party defected from cabinet"
        ),
    )
    party_id_source = models.CharField(blank=True, max_length=200)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    def clean(self):
        """Validation methods data before save."""
        validation.check_cabinet_party_countries(self)
        validation.check_cabinet_party_no_second_pm(self)

        return super().clean()  # pragma: no cover

    def get_absolute_url(self):
        """Get url for cabinet object."""
        return self.cabinet.get_absolute_url()

    class Meta:
        db_table = "data_cabinet_party"
        ordering = ("cabinet", "-pm")
        constraints = [
            models.UniqueConstraint(
                fields=["cabinet", "party"],
                name="unique_cabinet_party",
            ),
        ]

    def __str__(self):
        country = self.cabinet.country.name_short.capitalize()
        year = self.cabinet.start_date.year
        party = self.party.name_short

        return f"Cabinet party {country} – {year} {party} ({self.id})"
