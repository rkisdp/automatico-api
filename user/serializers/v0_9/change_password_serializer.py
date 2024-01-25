from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
)

from users.models import UserModel


class ChangePasswordSerializer(ModelSerializer):
    current_password = CharField(
        write_only=True,
        min_length=9,
        trim_whitespace=False,
    )
    password = CharField(
        write_only=True,
        min_length=9,
        trim_whitespace=False,
    )
    password_confirm = CharField(
        write_only=True,
        min_length=9,
        trim_whitespace=False,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "current_password",
            "password",
            "password_confirm",
        )

    def validate_current_password(self, value):
        is_valid = self.instance.check_password(value)
        if not is_valid:
            raise ValidationError(_("Password do not match."))
        return value

    def validate_password(self, value):
        validate_password(value, self.instance)
        return value

    def validate(self, attrs):
        current_password = attrs.get("current_password")
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if current_password == password:
            raise ValidationError(
                {"password": _("Password cannot be the same as current.")}
            )

        if password != password_confirm:
            raise ValidationError(
                {"password_confirm": _("Passwords do not match.")}
            )

        return attrs

    def update(self, instance: UserModel, validated_data):
        password = validated_data.pop("password")
        del validated_data["password_confirm"]
        del validated_data["current_password"]

        instance.set_password(password)
        return super().update(instance, validated_data)
