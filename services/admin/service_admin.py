from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from services.admin.inlines import ServiceHistoryInline
from services.models import Service


@register(Service)
class ServiceAdmin(ModelAdmin):
    search_help_text = "Vehicle plate or workshop name"
    show_full_result_count = True
    list_per_page = 25

    list_display = (
        "vehicle",
        "workshop",
        "description",
    )
    search_fields = ("vehicle__plate", "workshop__name")
    readonly_fields = (
        "vehicle",
        "workshop",
        "description",
        "created_at",
        "closed_at",
    )

    date_hierarchy = "created_at"

    fieldsets = (
        (
            "Service information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "vehicle",
                    "workshop",
                    "description",
                ),
            },
        ),
        (
            "Service dates",
            {
                "classes": ("extrapretty",),
                "fields": ("created_at", "closed_at"),
            },
        ),
    )

    inlines = (ServiceHistoryInline,)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
