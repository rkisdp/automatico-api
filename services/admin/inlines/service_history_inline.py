from django.contrib.admin import TabularInline

from services.models import ServiceHistory


class ServiceHistoryInline(TabularInline):
    model = ServiceHistory
    extra = 0
    verbose_name = "history"
    verbose_name_plural = "histories"

    fields = ("status", "comment", "responsable", "created_at")
    readonly_fields = ("created_at",)
