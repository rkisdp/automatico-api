from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import UserModel


class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["email"]

    def validate_email(self, value):
        user: UserModel = get_user_model().objects.filter(email__iexact=value)

        if not user.exists():
            raise serializers.ValidationError("User does not exist.")

        return value

    def update(self, instance, validated_data):
        email = validated_data["email"]
        user: UserModel = get_user_model().objects.get(email__iexact=email)

        temp_password = get_user_model().objects.make_random_password()
        user.set_password(temp_password)
        user.email_user(
            subject="Password reset",
            message=f"Your temporary password is: {temp_password}",
        )
        user.save()
        return user
