"""Define run script (django-extensions) to import ParlGov data.

Import ParlGov data into Django models using 'django-import-export'.

Script is only used in a development environment to create a fixture and needs
the 'django-import-export' package, specified as a development dependency.
"""

import os
from pathlib import Path, PosixPath

from import_export import resources
from tablib import Dataset

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db.models import Model


def get_data_files(path: PosixPath) -> list[str]:
    """Get names of all csv data files."""
    return sorted([dt for dt in os.listdir(path) if "csv" in dt])


def get_model(data_file: str) -> Model:
    """Get a model by 'app' and 'model' from file name.

    Use 'index__app__model.csv' file name elements to determine
    'app' and 'model'.
    """
    app_model = data_file.replace(".csv", "").split("__")
    django_model = apps.get_model(app_model[1], app_model[2])

    return django_model


def import_files_from_folder(path: PosixPath) -> None:
    """Import csv files with Django models."""
    for data_file in get_data_files(path):
        print(f"Importing '{data_file}' data")

        with open(path / data_file) as dt:
            dataset = Dataset().load(dt)

        django_model = get_model(data_file)
        import_resource = resources.modelresource_factory(model=django_model)()
        import_resource.import_data(dataset, raise_errors=True)


class Command(BaseCommand):
    """Create custom command ('./manage.py')."""

    help = "Import migrated data tables from legacy ParlGov database"

    def handle(self, *args, **options):
        """Define custom command actions."""
        print("\nCreating clean database to avoid orphaned data.\n")
        import_data_path = (
            Path(os.getcwd()).parent / "scripts/migrate_parlgov-db/import-data-legacy/"
        )
        import_files_from_folder(import_data_path)
