from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField


class WorkshopEmployeeListSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        read_only=True,
        use_url=True,
        help_text=_("URL to the user's photo."),
    )
    url = HyperLinkSelfField(
        view_name="users:users-detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
        help_text=_("URL to the user."),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "photo",
            "phone_number",
            "url",
        )
        read_only_fields = (
            "first_name",
            "last_name",
            "email",
            "photo",
            "phone_number",
        )
