from django.contrib.auth import get_user_model
from rest_framework import serializers

from security.models import VerificationCodeModel
from users.models import UserModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "photo",
        )

        read_only_fields = ("id", "photo")

    def update(self, instance: UserModel, validated_data):
        email = validated_data.pop("email", None)
        if email and email.lower() != instance.email:
            instance.email = email
            instance.email_verified = False
            instance.save()
            VerificationCodeModel.objects.create(
                user=instance, type__code="EVC"
            )

        return super().update(instance, validated_data)
