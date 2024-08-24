from django.contrib import admin

from .models import Election, ElectionResult


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "date",
        "type",
        "country",
        "id",
    )
    list_filter = (
        "type",
        "country",
    )
    search_fields = (
        "id",
        "country__name",
        "country__name_short",
        "date",
        "type__short",
        "data_json",
    )


@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "election",
        "party",
        "party_id_source",
        "id",
    )
    list_filter = (
        "election__type",
        "election__country",
    )
    autocomplete_fields = (
        "election",
        "party",
        "alliance",
    )
    search_fields = (
        "election__date",
        "party_id_source",
        "description",
        "comment",
        "data_json",
    )
