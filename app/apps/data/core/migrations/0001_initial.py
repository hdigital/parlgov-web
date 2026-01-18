import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "name_short",
                    models.CharField(db_index=True, max_length=3, unique=True),
                ),
                ("flag", models.CharField(max_length=2)),
                ("code_iso2", models.CharField(max_length=2, unique=True)),
                ("eu_accession_date", models.DateField(blank=True, null=True)),
                ("oecd_accession_date", models.DateField(blank=True, null=True)),
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
            ],
            options={
                "db_table": "data_country",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Code",
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
                    "table_variable",
                    models.CharField(
                        choices=[
                            ("party_family", "party — family_id"),
                            ("party_change_type", "party change — type_id"),
                            ("election_type", "election — type_id"),
                            ("election_ep_type", "election ep — type_id"),
                            ("cabinet_termination", "cabinet — termination_id"),
                            ("cabinet_support", "cabinet_support — type_id"),
                            ("confidence_vote", "confidence_vote — type_id"),
                            ("news_type", "news — type_id"),
                        ],
                        db_index=True,
                        max_length=100,
                    ),
                ),
                ("order", models.PositiveIntegerField(db_index=True)),
                ("short", models.SlugField(max_length=25)),
                ("name", models.CharField(max_length=50)),
                ("wikipedia", models.URLField(blank=True)),
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
            ],
            options={
                "db_table": "data_code",
                "ordering": ("table_variable", "order"),
                "constraints": [
                    models.UniqueConstraint(
                        fields=("table_variable", "short"),
                        name="unique_short_name_per_table",
                    )
                ],
            },
        ),
    ]
