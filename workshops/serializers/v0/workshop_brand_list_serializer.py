from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from vehicles.models import VehicleBrandModel


class WorkshopBrandListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        help_text=_("Name of the vehicle brand."),
    )
    image_url = serializers.ImageField(
        help_text=_("Image of the vehicle brand."),
        read_only=True,
        source="image",
        use_url=True,
    )

    class Meta:
        model = VehicleBrandModel
        fields = (
            "id",
            "name",
            "image_url",
        )
        read_only_fields = ("id",)
