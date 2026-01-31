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
            name="News",
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
                ("date", models.DateField()),
                (
                    "author",
                    models.CharField(
                        blank=True,
                        help_text="lowercase initials of author(s) name(s) (e.g. 'hd/pm')",
                        max_length=100,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "content",
                    models.TextField(
                        help_text="use Markdown markup language to structure the text"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.country",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        limit_choices_to={"table_variable": "news_type"},
                        on_delete=django.db.models.deletion.PROTECT,
                        to="datacore.code",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "news",
                "db_table": "docs_news",
                "ordering": ("-date", "-id"),
            },
        ),
        migrations.CreateModel(
            name="Page",
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
                ("page", models.SlugField()),
                ("section", models.SlugField(blank=True)),
                ("content", models.TextField()),
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
                "db_table": "docs_page",
                "ordering": ("page", "section"),
                "unique_together": {("page", "section")},
            },
        ),
    ]
