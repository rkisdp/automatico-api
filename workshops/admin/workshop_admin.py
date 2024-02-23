from django.contrib.gis.admin import GISModelAdmin, register

from workshops.models import Workshop


@register(Workshop)
class WorkshopAdmin(GISModelAdmin):
    search_help_text = (
        "You can search by owner first name, owner last name, name, "
        "specialities, vehicles, vehicles brand, vehicles model, vehicles "
        "year, vehicles nickname, vehicles vin."
    )
    show_full_result_count = True
    list_per_page = 25
    filter_horizontal = ("employees", "specialities", "vehicles", "brands")

    list_display = ("name", "owner")
    search_fields = (
        "owner__first_name",
        "owner__last_name",
        "name",
        "specialities__name",
        "vehicles__brand__name",
        "vehicles__model",
        "vehicles__year",
        "vehicles__nickname",
        "vehicles__vin",
    )

    fieldsets = (
        (
            "Workshop information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "name",
                    "location",
                    "employees",
                    "brands",
                    "specialities",
                    "vehicles",
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
        return ()
