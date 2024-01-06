from django.contrib.auth import get_user_model
from rest_framework import serializers


class ProfileImageSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        allow_empty_file=False, allow_null=False, required=True
    )

    class Meta:
        model = get_user_model()
        fields = ("photo",)
