from django.contrib.auth import get_user_model
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "default_password",
            "role",
            "role_id",
            "is_active",
            "status",
        ]

        read_only_fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "default_password",
            "is_active",
            "role_id",
        ]
