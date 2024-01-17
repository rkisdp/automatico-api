from django.contrib.admin import ModelAdmin, register

from services.models import ServiceStatusModel


@register(ServiceStatusModel)
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
