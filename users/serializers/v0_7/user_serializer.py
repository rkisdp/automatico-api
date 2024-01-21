from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
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
            "is_active",
            "is_staff",
            "date_joined",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "photo",
            "phone_number_verified",
        )
