from django.contrib.admin import ModelAdmin, register

from workshops.models import Speciality


@register(Speciality)
class SpecialityAdmin(ModelAdmin):
    search_help_text = "Speciality"
    show_full_result_count = True
    list_per_page = 25

    list_display = ("name",)
    search_fields = ("name",)

    fieldsets = (
        (
            "Speciality information",
            {
                "classes": ("extrapretty",),
                "fields": ("name", "image"),
            },
        ),
    )
