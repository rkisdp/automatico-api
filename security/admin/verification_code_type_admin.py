from django.contrib.admin import ModelAdmin, register

from security.models import VerificationCodeTypeModel


@register(VerificationCodeTypeModel)
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
            return self.readonly_fields + ("code", "name")
        return self.readonly_fields
