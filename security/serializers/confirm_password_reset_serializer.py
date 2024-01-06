from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from security.email import CodeValidator


class ConfirmPasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    code = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        email = validated_data.get("email")
        users = get_user_model().objects.filter(
            email__iexact=email, is_active=True, email_verified=True
        )

        if not users.exists():
            raise serializers.ValidationError(
                {
                    "email": "A user with that email does not exist, is not"
                    " active, does not have a verified email"
                }
            )

        code = validated_data.get("code")
        user = users.first()
        CodeValidator.run_validations(user, code, "PRC")

        password = validated_data.get("password")
        password_confirm = validated_data.get("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )

        if user.check_password(password):
            raise serializers.ValidationError(
                {"password": "Password cannot be the same as the old one"}
            )

        try:
            validate_password(password, user=user)
        except ValidationError as e:
            raise ValidationError({"password": e.messages})

        user.set_password(password)
        user.save()

        CodeValidator.delete_verification_code(user)
        return validated_data
