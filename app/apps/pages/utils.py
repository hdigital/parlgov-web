"""Utilities for 'pages' app."""

from collections import namedtuple

from django.apps import apps


def get_data_count():
    """Count the number of observations."""
    Model = namedtuple("Model", ["app", "name"])

    models = (
        Model("datacore", "Country"),
        Model("parties", "Party"),
        Model("elections", "Election"),
        Model("elections", "ElectionResult"),
        Model("cabinets", "Cabinet"),
        Model("cabinets", "CabinetParty"),
    )

    count = {}
    for model in models:
        model_instance = apps.get_model(model.app, model.name)
        count[model.name] = model_instance.objects.all().count()

    return count
