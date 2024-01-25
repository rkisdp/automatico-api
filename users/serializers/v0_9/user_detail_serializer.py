from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_9 import HyperLinkSelfField


class UserDetailSerializer(serializers.ModelSerializer):
    workshops = serializers.IntegerField(
        read_only=True,
        source="workshops.count",
        default=0,
    )
    workshops_url = HyperLinkSelfField(
        view_name="users:workshops",
        lookup_field="id",
        lookup_url_kwarg="user_id",
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
            "workshops",
            "workshops_url",
            "photo_url",
            "url",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
        )
