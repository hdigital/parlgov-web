from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from ...base.models import (
    BaseModel,
    comment_help_text,
    data_json_help_text,
    description_help_text,
)
from ..core.helptext import data_source_help_text
from . import validation


class Election(BaseModel):
    """Election information."""

    type = models.ForeignKey(
        "datacore.Code",
        db_column="type_id",
        default=13,
        limit_choices_to={"table_variable": "election_type"},
        on_delete=models.PROTECT,
    )
    country = models.ForeignKey("datacore.Country", on_delete=models.PROTECT)
    date = models.DateField(db_index=True)
    early = models.BooleanField(default=False)
    wikipedia = models.URLField(null=True, blank=True, max_length=200)
    dissolution_date = models.DateField(null=True, blank=True)
    seats_total = models.PositiveIntegerField(validators=[MaxValueValidator(1000)])
    electorate = models.PositiveIntegerField(null=True, blank=True)
    votes_cast = models.PositiveIntegerField(null=True, blank=True)
    votes_valid = models.PositiveIntegerField(null=True, blank=True)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    def get_absolute_url(self):
        """Get url for election object (parliament and EP)."""
        url_parameters = {"country": self.country.slug, "election_date": self.date}

        parliament = self.type.short == "parliament"
        election_view_name = "elections:detail" if parliament else "elections:detail_ep"

        return reverse(election_view_name, kwargs=url_parameters)

    @classmethod
    def get_by_date(cls, country, date, type_short="parliament"):
        """Get the election for a date (previous or same date)."""
        election = cls.objects.filter(
            country=country, date__lte=date, type__short=type_short
        )
        return election.last()

    class Meta:
        db_table = "data_election"
        ordering = ("country", "type", "date")
        constraints = [
            models.UniqueConstraint(
                fields=["country", "date", "type"],
                name="unique_election_country_date_election_type",
            ),
        ]

    def __str__(self):
        country = self.country.name_short.capitalize()
        ep_election = "EP " if self.type.short == "ep" else ""
        return f"Election {country} – {self.date.year} {ep_election}({self.id})"


class ElectionResult(BaseModel):
    """Election result for a party."""

    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
    )
    party = models.ForeignKey(
        "parties.Party",
        on_delete=models.PROTECT,
    )
    party_id_source = models.CharField(blank=True, max_length=200)
    alliance = models.ForeignKey(
        "self",
        related_name="alliance_set",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=(
            "'election_result_id' of electoral alliance "
            "party belongs to in this election"
        ),
    )
    seats = models.PositiveIntegerField(
        null=True,
        blank=True,
        db_index=True,
        validators=[MaxValueValidator(1000)],
        help_text=(
            "enter '0' if the party won no seats -- "
            "leave empty for alliances were seats are coded for members"
        ),
    )
    vote_share = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(Decimal(0)),
            MaxValueValidator(Decimal(100)),
        ],
        help_text=("official vote share -- max. two  decimal places"),
    )
    votes = models.PositiveIntegerField(null=True, blank=True)
    data_source = models.CharField(
        blank=True, max_length=200, help_text=data_source_help_text
    )
    description = models.TextField(blank=True, help_text=description_help_text)
    comment = models.TextField(blank=True, help_text=comment_help_text)
    data_json = models.JSONField(
        default=dict, blank=True, help_text=data_json_help_text
    )

    @property
    def seat_share(self):
        """Provide seat share as class property."""
        if self.seats and self.election.seats_total:
            return float(self.seats) / float(self.election.seats_total) * 100.0

    def clean(self):
        """Validate data on safe."""
        validation.check_election_party_countries(self)
        if self.alliance:
            validation.check_alliance_no_self_reference(self)
            validation.check_alliance_election_ids_equal(self)

        return super().clean()

    def get_absolute_url(self):
        """Get url for election result object (parliament and EP)."""
        return self.election.get_absolute_url()

    class Meta:
        db_table = "data_election_result"
        ordering = ("election", "-seats", "-vote_share")
        constraints = [
            models.UniqueConstraint(
                fields=["election", "party"],
                name="unique_election_result_party",
            ),
        ]

    def __str__(self):
        country = self.election.country.name_short.capitalize()
        year = self.election.date.year
        ep_election = "EP " if self.election.type.short == "ep" else ""
        party = self.party.name_short

        return f"Election result {country} – {year} {ep_election}{party} ({self.id})"
