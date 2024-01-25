from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_9 import HyperLinkSelfField


class UserListSerializer(serializers.ModelSerializer):
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
            "services_url",
            "vehicles_url",
            "workshops_url",
            "workshops_services_url",
            "url",
        )
        read_only_fields = ("id",)
