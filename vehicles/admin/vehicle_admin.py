from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from vehicles.models import Vehicle


@register(Vehicle)
class VehicleAdmin(ModelAdmin):
    search_help_text = "Brand, model, nickname, owner, VIN"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("brand", "model", "year", "owner")
    search_fields = (
        "brand__name",
        "model",
        "nickname",
        "owner__first_name",
        "owner__last_name",
        "vin",
    )

    fieldsets = (
        (
            "Vehicle information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "brand",
                    "model",
                    "year",
                    "nickname",
                    "vin",
                ),
            },
        ),
        (
            "Owner information",
            {
                "classes": ("extrapretty",),
                "fields": ("owner",),
            },
        ),
        (
            "Other information",
            {
                "classes": ("extrapretty",),
                "fields": ("image",),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("owner",)
        return super().get_readonly_fields(request, obj)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser
