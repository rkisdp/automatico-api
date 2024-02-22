from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import ReviewImageModel


class WorkshopImageSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        write_only=True,
        child=serializers.ImageField(
            allow_empty_file=False,
            allow_null=False,
            required=False,
        ),
    )
    image_url = serializers.ListField(
        read_only=True,
        child=serializers.ImageField(use_url=True),
    )

    class Meta:
        model = ReviewImageModel
        fields = (
            "image",
            "image_url",
        )
