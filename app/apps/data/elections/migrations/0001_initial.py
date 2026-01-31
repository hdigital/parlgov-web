import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("datacore", "0001_initial"),
        ("parties", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Election",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(db_index=True)),
                ("early", models.BooleanField(default=False)),
                ("wikipedia", models.URLField(blank=True, null=True)),
                ("dissolution_date", models.DateField(blank=True, null=True)),
                (
                    "seats_total",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(1000)]
                    ),
                ),
                ("electorate", models.PositiveIntegerField(blank=True, null=True)),
                ("votes_cast", models.PositiveIntegerField(blank=True, null=True)),
                ("votes_valid", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "data_source",
                    models.CharField(
                        blank=True,
                        help_text="list of data sources separated by a comma",
                        max_length=200,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="information about the observation"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="comments about the coding of this observation",
                    ),
                ),
                (
                    "data_json",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text='additional data saved as key-value pairs in JSON format\n                         — use "{}" for empty json fields',
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.country",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        db_column="type_id",
                        default=13,
                        limit_choices_to={"table_variable": "election_type"},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.code",
                    ),
                ),
            ],
            options={
                "db_table": "data_election",
                "ordering": ("country", "type", "date"),
            },
        ),
        migrations.CreateModel(
            name="ElectionResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("party_id_source", models.CharField(blank=True, max_length=200)),
                (
                    "seats",
                    models.PositiveIntegerField(
                        blank=True,
                        db_index=True,
                        help_text="enter '0' if the party won no seats -- leave empty for alliances were seats are coded for members",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(1000)],
                    ),
                ),
                (
                    "vote_share",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="official vote share -- max. two  decimal places",
                        max_digits=5,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0")),
                            django.core.validators.MaxValueValidator(Decimal("100")),
                        ],
                    ),
                ),
                ("votes", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "data_source",
                    models.CharField(
                        blank=True,
                        help_text="list of data sources separated by a comma",
                        max_length=200,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="information about the observation"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="comments about the coding of this observation",
                    ),
                ),
                (
                    "data_json",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text='additional data saved as key-value pairs in JSON format\n                         — use "{}" for empty json fields',
                    ),
                ),
                (
                    "alliance",
                    models.ForeignKey(
                        blank=True,
                        help_text="'election_result_id' of electoral alliance party belongs to in this election",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="alliance_set",
                        to="elections.electionresult",
                    ),
                ),
                (
                    "election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.election",
                    ),
                ),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="parties.party"
                    ),
                ),
            ],
            options={
                "db_table": "data_election_result",
                "ordering": ("election", "-seats", "-vote_share"),
            },
        ),
        migrations.AddConstraint(
            model_name="election",
            constraint=models.UniqueConstraint(
                fields=("country", "date", "type"),
                name="unique_election_country_date_election_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="electionresult",
            constraint=models.UniqueConstraint(
                fields=("election", "party"), name="unique_election_result_party"
            ),
        ),
    ]
