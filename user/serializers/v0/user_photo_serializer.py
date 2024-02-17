from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserPhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        allow_empty_file=False,
        allow_null=False,
        required=True,
    )
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
    )

    class Meta:
        model = get_user_model()
        fields = ("image", "image_url")
