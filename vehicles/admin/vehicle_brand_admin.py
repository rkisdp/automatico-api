from django.contrib.admin import ModelAdmin, register

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
            "Personal information",
            {
                "classes": ("extrapretty",),
                "fields": ("name",),
            },
        ),
    )
