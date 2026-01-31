import apps.data.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("datacore", "0001_initial"),
        ("elections", "0001_initial"),
        ("parties", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cabinet",
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
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                ("start_date", models.DateField(db_index=True)),
                ("termination_date", models.DateField(blank=True, null=True)),
                ("caretaker", models.BooleanField(default=False)),
                ("wikipedia", models.URLField(blank=True, null=True)),
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
                    "election",
                    models.ForeignKey(
                        blank=True,
                        help_text="previous election — value is added or updated on save",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.election",
                    ),
                ),
            ],
            options={
                "db_table": "data_cabinet",
                "ordering": ("country", "start_date"),
            },
        ),
        migrations.CreateModel(
            name="CabinetParty",
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
                ("pm", models.BooleanField(default=False)),
                (
                    "defector",
                    models.BooleanField(
                        default=False,
                        help_text="Add information in description field why party defected from cabinet",
                    ),
                ),
                ("party_id_source", models.CharField(blank=True, max_length=200)),
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
                    "cabinet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cabinets.cabinet",
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
                "db_table": "data_cabinet_party",
                "ordering": ("cabinet", "-pm"),
            },
        ),
        migrations.AddConstraint(
            model_name="cabinet",
            constraint=models.UniqueConstraint(
                fields=("country", "name"), name="unique_cabinet_name_per_country"
            ),
        ),
        migrations.AddConstraint(
            model_name="cabinet",
            constraint=models.UniqueConstraint(
                fields=("country", "start_date"), name="unique_cabinet_date_per_country"
            ),
        ),
        migrations.AddConstraint(
            model_name="cabinet",
            constraint=models.CheckConstraint(
                condition=models.Q(("start_date__lte", models.F("termination_date"))),
                name="cabinet_start_date_smaller_than_termination_date",
            ),
        ),
        migrations.AddConstraint(
            model_name="cabinetparty",
            constraint=models.UniqueConstraint(
                fields=("cabinet", "party"), name="unique_cabinet_party"
            ),
        ),
    ]
