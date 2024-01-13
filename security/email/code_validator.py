from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from security.models import VerificationCodeModel


def _raise_validation_error(message: str) -> None:
    raise serializers.ValidationError({"code": _(message)})


class CodeValidator:
    @staticmethod
    def run_validations(user, code: str, type: str) -> None:
        if not hasattr(user, "verification_code"):
            _raise_validation_error("Invalid or expired validation code")

        verification_code: VerificationCodeModel = user.verification_code
        if (
            verification_code.type.code != type
            and verification_code.type.code != f"R{type}"
        ):
            _raise_validation_error("Invalid or expired validation code")

        if not check_password(code, verification_code.code):
            _raise_validation_error("Invalid or expired validation code")

        if not verification_code.is_valid:
            _raise_validation_error("Invalid or expired validation code")

    @staticmethod
    def delete_verification_code(user) -> None:
        verification_code: VerificationCodeModel = user.verification_code
        verification_code.delete()
