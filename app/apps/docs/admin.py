from django.contrib import admin

from .models import News, Page


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "date",
        "author",
        "title",
        "country",
        "type",
        "id",
    )
    list_filter = ("type",)
    search_fields = (
        "title",
        "content",
    )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        "page",
        "section",
        "id",
    )
    list_filter = ("page",)
    search_fields = (
        "page",
        "section",
    )
