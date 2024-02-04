from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from security.email import send_verification_code
from security.models import VerificationCodeModel


class ResendEmailVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        users = get_user_model().objects.filter(email__iexact=email)

        if not users.exists():
            raise serializers.ValidationError(
                {"email": _("A user with that email does not exist.")}
            )

        user = users.first()
        if not user.is_active:
            raise serializers.ValidationError(
                {"email": _("Account is not active.")}
            )

        if user.email_verified:
            raise serializers.ValidationError(
                {"email": _("Email is already verified.")}
            )

        verification_codes = VerificationCodeModel.objects.filter(user=user)
        if verification_codes.exists():
            verification_codes.delete()

        send_verification_code(
            user=user,
            code_type="REVC",
            email_template="email_verification_code",
            email_subject="Verificación de Correo Electrónico",
        )
        return attrs
