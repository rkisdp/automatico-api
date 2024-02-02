from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from security.email import CodeValidator


class EmailVerificationSerializer(serializers.Serializer):
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
        if user.email_verified:
            raise serializers.ValidationError(
                {"email": _("Email is already verified.")}
            )

        CodeValidator.run_validations(user, code, "EVC")

        user.email_verified = True
        user.save()

        CodeValidator.delete_verification_code(user)
        return attrs
