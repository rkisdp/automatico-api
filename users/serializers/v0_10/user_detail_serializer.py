from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
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
            "image_url",
            "url",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
        )
