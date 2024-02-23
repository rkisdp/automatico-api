from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import Workshop


class WorkshopImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        write_only=True,
        allow_empty_file=False,
        allow_null=False,
        required=True,
    )
    image_url = serializers.ImageField(
        use_url=True,
        read_only=True,
        source="image",
    )

    class Meta:
        model = Workshop
        fields = (
            "image",
            "image_url",
        )
