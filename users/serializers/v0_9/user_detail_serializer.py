from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_9 import HyperLinkSelfField


class UserDetailSerializer(serializers.ModelSerializer):
    services_url = HyperLinkSelfField(
        view_name="user:services",
    )
    vehicles_url = HyperLinkSelfField(
        view_name="user:vehicles",
    )
    workshops_url = HyperLinkSelfField(
        view_name="user:workshops",
    )
    workshops_services_url = HyperLinkSelfField(
        view_name="user:workshops-services",
    )
    photo_url = serializers.ImageField(
        read_only=True,
        source="photo",
        use_url=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "services_url",
            "vehicles_url",
            "workshops_url",
            "workshops_services_url",
            "photo_url",
            "url",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
        )
