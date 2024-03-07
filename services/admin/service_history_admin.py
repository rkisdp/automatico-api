from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from services.models import ServiceHistory


@register(ServiceHistory)
class ServiceHistoryAdmin(ModelAdmin):
    search_help_text = "Workshop name or service status"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("service", "status", "comment", "responsable")
    search_fields = ("service__workshop__name", "service__status__name")
    readonly_fields = ("service", "comment", "responsable", "created_at")

    date_hierarchy = "created_at"

    fieldsets = (
        (
            "Service history information",
            {
                "classes": ("extrapretty",),
                "fields": ("service", "status", "comment", "responsable"),
            },
        ),
        (
            "Service history dates",
            {
                "classes": ("extrapretty",),
                "fields": ("created_at",),
            },
        ),
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
