from django.contrib.admin import ModelAdmin, register
from django.http import HttpRequest

from vehicles.models import VehicleBrand


@register(VehicleBrand)
class VehicleBrandAdmin(ModelAdmin):
    search_help_text = "Name"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("name",)
    search_fields = ("name",)

    fieldsets = (
        (
            "Brand information",
            {
                "classes": ("extrapretty",),
                "fields": ("name", "image"),
            },
        ),
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_superuser

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser
