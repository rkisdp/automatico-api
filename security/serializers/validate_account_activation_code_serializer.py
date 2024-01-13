from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from security.email import CodeValidator


class ValidateAccountActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=255,
        write_only=True,
    )
    code = serializers.CharField(
        min_length=4,
        max_length=4,
        write_only=True,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        code = attrs.get("code")
        user = get_user_model().objects.filter(email__iexact=email)

        if not user.exists():
            raise serializers.ValidationError(
                {"email": _("A user with that email does not exist.")}
            )

        user = user.first()
        if user.is_active:
            raise serializers.ValidationError(
                {"email": _("Account is already active.")}
            )

        CodeValidator.run_validations(user, code, "AAC")
        return attrs
