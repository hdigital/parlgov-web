from django.contrib import admin

from .models import Party, PartyChange, PartyFamily, PartyNameChange


class PartyFamilyInline(admin.TabularInline):
    model = PartyFamily


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = (PartyFamilyInline,)
    list_display = (
        "name_short",
        "name_english",
        "name",
        "country",
        "id",
    )
    list_filter = (
        "country",
        "family",
    )
    search_fields = (
        "country__name_short",
        "country__name",
        "name_short",
        "name_english",
        "name",
        "data_json",
    )


@admin.register(PartyNameChange)
class PartyNameChangeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "party",
        "name_english",
        "name",
        "date",
        "id",
    )
    list_filter = ("party__country",)
    # raw_id_fields = ("party",)
    autocomplete_fields = ("party",)
    search_fields = (
        "date",
        "party__id",
        "name_short",
        "name_english",
        "name",
    )


@admin.register(PartyChange)
class PartyChangeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "party",
        "party_new",
        "date",
        "id",
    )
    list_filter = ("party__country",)
    # raw_id_fields = ("party", "party_new")
    autocomplete_fields = (
        "party",
        "party_new",
    )
    search_fields = (
        "party__id",
        "party__name_short",
        "party_new__id",
        "party_new__name_short",
    )
