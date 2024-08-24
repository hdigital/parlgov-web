"""Base models for all apps in the project.

'description', 'comment', 'data_json' fields are used in some models.
No 'DataModel' base model with these fields is used to keep columns and fields
ordered in the database and the Django admin.
"""

from django.db import models
from django.utils import timezone

markdown_help_text = "use Markdown markup language to structure the text"

description_help_text = "information about the observation"
comment_help_text = "comments about the coding of this observation"
data_json_help_text = """additional data saved as key-value pairs in JSON format
                         — use "{}" for empty json fields"""


class BaseModel(models.Model):
    """Base model with default fields 'created_at' and 'updated_at'."""

    created_at = models.DateTimeField(
        db_index=True, default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
