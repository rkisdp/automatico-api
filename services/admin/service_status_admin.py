from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from services.models import ServiceStatus


@register(ServiceStatus)
class ServiceStatusAdmin(ModelAdmin):
    search_help_text = "Service status"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("name",)
    search_fields = ("name",)

    fieldsets = (
        (
            "Service status information",
            {
                "classes": ("extrapretty",),
                "fields": ("name",),
            },
        ),
    )

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser
