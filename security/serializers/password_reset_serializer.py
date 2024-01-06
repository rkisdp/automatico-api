from django.contrib.auth import get_user_model
from rest_framework import serializers

from security.email import send_verification_code


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def validate(self, validated_data):
        email = validated_data.get("email")
        users = get_user_model().objects.filter(
            email__iexact=email, is_active=True, email_verified=True
        )

        if not users.exists():
            raise serializers.ValidationError(
                {
                    "email": "A user with that email does not exist, is not"
                    " active or does not have a verified email"
                }
            )

        send_verification_code(
            user=users.first(),
            code_type="PRC",
            email_template="password_reset_code",
            email_subject="Reinicio de Contraseña",
        )
        return validated_data
