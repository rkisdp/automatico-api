from django.contrib.admin import ModelAdmin, register

from services.admin.inlines import ServiceHistoryInline
from services.models import ServiceModel


@register(ServiceModel)
class ServiceAdmin(ModelAdmin):
    search_help_text = "Vehicle plate or workshop name"
    show_full_result_count = True
    list_per_page = 25

    list_display = (
        "vehicle",
        "workshop",
        "request_description",
        "response_description",
    )
    search_fields = ("vehicle__plate", "workshop__name")
    readonly_fields = ("start_date", "end_date")

    date_hierarchy = "start_date"

    fieldsets = (
        (
            "Service information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "vehicle",
                    "workshop",
                    "request_description",
                    "response_description",
                ),
            },
        ),
        (
            "Service dates",
            {
                "classes": ("extrapretty",),
                "fields": ("start_date", "end_date"),
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
                    "request_description",
                    "response_description",
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
                "request_description",
                "response_description",
            )
        return self.readonly_fields
