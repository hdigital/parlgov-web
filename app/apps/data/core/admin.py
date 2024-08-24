from django.contrib import admin

from .models import Code, Country


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "table_variable",
        "order",
        "short",
        "name",
        "id",
    )
    list_filter = ("table_variable",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "name_short",
        "name",
        "flag",
        "id",
    )
    search_fields = (
        "name_short",
        "name",
        "data_json",
    )
