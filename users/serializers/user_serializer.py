from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField(default=1)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
            "role_id",
            "is_active",
            "status",
        ]

        read_only_fields = ["id"]

    def validate_role_id(self, value: int) -> int:
        if value not in [1, 2]:
            raise serializers.ValidationError(
                {"role_id": "role_id must be 1 (admin) or 2 (cobrador)"}
            )
        return value

    def create(self, validated_data) -> UserModel:
        role_id = validated_data.pop("role_id")

        validated_data["groups"] = [role_id]

        instance: UserModel = super().create(validated_data)

        temp_password = get_user_model().objects.make_random_password()

        instance.email_user(
            subject="Welcome to Loans!",
            message=f"Your temporary password is: {temp_password}",
        )

        instance.set_password(temp_password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        role_id = validated_data.pop("role_id")

        validated_data["groups"] = [role_id]
        return super().update(instance, validated_data)
