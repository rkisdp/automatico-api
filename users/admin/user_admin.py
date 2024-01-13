from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@register(get_user_model())
class UserAdmin(BaseUserAdmin):
    search_help_text = "First name, last name and email."
    show_full_result_count = True
    list_per_page = 25
    date_hierarchy = "date_joined"
    actions = ("activate_user", "deactivate_user")

    ordering = (
        "first_name",
        "last_name",
        "email",
    )
    list_display = (
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )

    add_fieldsets = (
        (
            "Personal information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "first_name",
                    "last_name",
                    "photo",
                ),
            },
        ),
        (
            "Auth information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    fieldsets = (
        (
            "Personal information",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "first_name",
                    "last_name",
                    "photo",
                ),
            },
        ),
        (
            "Auth information",
            {
                "classes": ("extrapretty",),
                "fields": ("email",),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Others",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "date_joined",
                    "last_login",
                ),
            },
        ),
    )
