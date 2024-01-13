from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        label="Confirm password", write_only=True, min_length=9
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        )

        read_only_fields = ("id",)
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 9,
            },
        }

    def validate_username(self, value: str) -> str:
        user = get_user_model().objects.filter(username__iexact=value)
        if user.exists():
            raise serializers.ValidationError(
                "A user with that username already exists."
            )
        return value

    def validate_email(self, value: str) -> str:
        user = get_user_model().objects.filter(email__iexact=value)
        if user.exists():
            raise serializers.ValidationError(
                "A user with that email already exists."
            )
        return value

    def validate_password(self, value: str) -> str:
        validate_password(value)
        return value

    def validate(self, attrs: dict) -> dict:
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
