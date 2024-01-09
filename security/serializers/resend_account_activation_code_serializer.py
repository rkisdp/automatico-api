from django.contrib.auth import get_user_model
from rest_framework import serializers

from security.email import send_verification_code


class ResendAccountActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        users = get_user_model().objects.filter(email__iexact=email)

        if not users.exists():
            raise serializers.ValidationError(
                {"email": "A user with that email does not exist."}
            )

        user = users.first()
        if user.is_active:
            raise serializers.ValidationError(
                {"email": "Account is already active."}
            )

        send_verification_code(
            user=user,
            code_type="RAAC",
            email_template="account_activation_code",
            email_subject="Activación de Cuenta",
        )

        return attrs
