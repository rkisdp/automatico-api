from django.contrib.admin import ModelAdmin, register

from services.models import ServiceHistoryModel


@register(ServiceHistoryModel)
class ServiceHistoryAdmin(ModelAdmin):
    search_help_text = "Workshop name or service status"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("service", "status", "comment", "responsable")
    search_fields = ("service__workshop__name", "service__status__name")
    readonly_fields = ("created_at",)

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

    fieldsets_add = (
        (
            "Service history information",
            {
                "classes": ("extrapretty",),
                "fields": ("service", "status", "comment", "responsable"),
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.fieldsets_add

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("service", "comment", "responsable")
        return self.readonly_fields
