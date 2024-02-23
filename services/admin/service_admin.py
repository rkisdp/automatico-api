from django.contrib.admin import ModelAdmin, register

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
    readonly_fields = ("created_at", "closed_at")

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

    fieldsets_add = (
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
    )

    inlines = (ServiceHistoryInline,)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.fieldsets_add

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + (
                "vehicle",
                "workshop",
                "description",
            )
        return self.readonly_fields
