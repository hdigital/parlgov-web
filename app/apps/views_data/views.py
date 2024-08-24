"""Create a CSV file for public database tables."""

import csv

from django.apps import apps
from django.db import connection
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


def get_public_db_tables() -> list[str]:
    """Get a list of public database tables, excluding Django tables."""
    tables_all = [model._meta.db_table for model in apps.get_models()]

    tables_public = [
        table
        for table in tables_all
        if table.startswith("data_") or table.startswith("docs_")
    ] + ["view_party", "view_election", "view_cabinet"]

    return tables_public


def check_db_table_is_public(db_table: str) -> bool:
    """Check if a database table is public."""
    return db_table in get_public_db_tables()


def fetch_data(db_table: str) -> tuple:
    """Fetch data from a database table.

    Parameter 'db_table' is checked to avoid SQL injection.
    """
    if not check_db_table_is_public(db_table):
        raise Exception("Table is not public")

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {db_table}")
        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]

    return rows, column_names


def csv_view(request: HttpRequest, db_table: str) -> HttpResponse:
    """Return CSV file for public database table."""
    if not check_db_table_is_public(db_table):
        return HttpResponseNotFound("<h1>Table not found</h1>")

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{db_table}.csv"'

    rows, column_names = fetch_data(db_table)
    writer = csv.writer(response)
    writer.writerow(column_names)
    for row in rows:  # pragma: no cover
        writer.writerow(row)

    return response
