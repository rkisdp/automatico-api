from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from security.models import VerificationCodeType


@register(VerificationCodeType)
class VerificationCodeTypeAdmin(ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")
    ordering = ("code",)
    fieldsets = (
        (
            "Code Type Information",
            {
                "fields": (
                    "code",
                    "name",
                    "description",
                )
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("code", "name") + self.readonly_fields
        return self.readonly_fields

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
