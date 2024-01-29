from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
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
            "full_name",
            "email",
            "phone_number",
            "photo_url",
            "url",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
        )
