import apps.data.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("datacore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Party",
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
                    "name_short",
                    models.CharField(
                        db_index=True,
                        max_length=10,
                        validators=[
                            apps.data.core.validators.validate_ascii,
                            apps.data.core.validators.validate_no_space,
                        ],
                    ),
                ),
                (
                    "name_english",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=200)),
                (
                    "name_ascii",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                ("name_nonlatin", models.CharField(blank=True, max_length=200)),
                ("wikipedia", models.URLField(blank=True, null=True)),
                (
                    "foundation_date",
                    models.DateField(
                        blank=True,
                        help_text="'xxxx-07-01' for known year and unknown month/day —\n                     data_json 'xyz_date = true' for exact date on 'xxxx-07-01'",
                        null=True,
                    ),
                ),
                ("dissolution_date", models.DateField(blank=True, null=True)),
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
                    "family",
                    models.ForeignKey(
                        db_column="family_id",
                        limit_choices_to={
                            "order__lt": 200,
                            "table_variable": "party_family",
                        },
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.code",
                    ),
                ),
            ],
            options={
                "db_table": "data_party",
                "ordering": ("country", "name_ascii"),
            },
        ),
        migrations.CreateModel(
            name="PartyChange",
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
                    "date",
                    models.DateField(
                        db_index=True,
                        help_text="'xxxx-07-01' for known year and unknown month/day —\n                     data_json 'xyz_date = true' for exact date on 'xxxx-07-01'",
                    ),
                ),
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
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partychange_set",
                        to="parties.party",
                    ),
                ),
                (
                    "party_new",
                    models.ForeignKey(
                        db_column="party_id_new",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partychange_new_set",
                        to="parties.party",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        db_column="type_id",
                        limit_choices_to={"table_variable": "party_change_type"},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datacore.code",
                    ),
                ),
            ],
            options={
                "db_table": "data_party_change",
                "ordering": ("date",),
            },
        ),
        migrations.CreateModel(
            name="PartyFamily",
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
                    "family",
                    models.ForeignKey(
                        db_column="type_id",
                        limit_choices_to={"table_variable": "party_family"},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.code",
                    ),
                ),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="parties.party"
                    ),
                ),
            ],
            options={
                "db_table": "data_party_family",
            },
        ),
        migrations.CreateModel(
            name="PartyNameChange",
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
                    "date",
                    models.DateField(
                        help_text="'xxxx-07-01' for known year and unknown month/day —\n                     data_json 'xyz_date = true' for exact date on 'xxxx-07-01'"
                    ),
                ),
                ("party_change", models.BooleanField(default=False)),
                (
                    "name_short",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                (
                    "name_english",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200)),
                (
                    "name_ascii",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        validators=[apps.data.core.validators.validate_ascii],
                    ),
                ),
                ("name_nonlatin", models.CharField(blank=True, max_length=200)),
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
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="parties.party"
                    ),
                ),
            ],
            options={
                "db_table": "data_party_name_change",
                "ordering": ("party", "date"),
            },
        ),
        migrations.AddConstraint(
            model_name="party",
            constraint=models.UniqueConstraint(
                fields=("country", "name_short"),
                name="unique_party_name_short_per_country",
            ),
        ),
        migrations.AddConstraint(
            model_name="partychange",
            constraint=models.CheckConstraint(
                condition=models.Q(("party", models.F("party_new")), _negated=True),
                name="party_and_party_new_not_equal",
            ),
        ),
    ]
