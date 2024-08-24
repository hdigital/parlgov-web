from django.template.response import TemplateResponse

from ...views_data.views import get_public_db_tables
from .models import Country


def data_index_view(request):
    """Index page of data with countries and tables links."""
    context = {
        "countries": Country.objects.all(),
        "tables": get_public_db_tables(),
    }

    return TemplateResponse(request, "data/data-index.html", context)
