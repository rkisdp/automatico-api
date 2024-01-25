from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="users:users-detail",
        lookup_field="id",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "email_verified",
            "photo",
            "phone_number",
            "phone_number_verified",
            "url",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
        )
