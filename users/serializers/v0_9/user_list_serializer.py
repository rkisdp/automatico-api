from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_9 import HyperLinkSelfField


class UserListSerializer(serializers.ModelSerializer):
    workshops_url = HyperLinkSelfField(
        view_name="users:workshops",
        lookup_field="id",
        lookup_url_kwarg="user_id",
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
            "workshops_url",
            "url",
        )
        read_only_fields = ("id",)
