from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserPhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        allow_empty_file=False,
        allow_null=False,
        required=True,
        use_url=True,
    )

    class Meta:
        model = get_user_model()
        fields = ("photo",)
