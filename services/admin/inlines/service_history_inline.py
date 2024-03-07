from django.contrib.admin import TabularInline
from django.http import HttpRequest

from services.models import ServiceHistory


class ServiceHistoryInline(TabularInline):
    model = ServiceHistory
    extra = 0
    verbose_name = "history"
    verbose_name_plural = "histories"
    can_delete = False

    fields = ("status", "comment", "responsable", "created_at")
    readonly_fields = fields

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
