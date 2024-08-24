from django.contrib import admin

from .models import Cabinet, CabinetParty


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "name",
        "start_date",
        "country",
        "id",
    )
    list_filter = ("country",)
    readonly_fields = ("election",)
    search_fields = (
        "id",
        "country__name",
        "country__name_short",
        "name",
        "start_date",
        "data_json",
    )


@admin.register(CabinetParty)
class CabinetPartyAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "party",
        "cabinet",
        "pm",
        "party_id_source",
        "id",
    )
    list_filter = ("cabinet__country",)
    raw_id_fields = (
        "cabinet",
        "party",
    )
    autocomplete_fields = (
        "cabinet",
        "party",
    )
    search_fields = (
        "cabinet__name",
        "party_id_source",
        "description",
        "comment",
        "data_json",
    )
