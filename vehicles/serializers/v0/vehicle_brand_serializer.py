from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from vehicles.models import VehicleBrand


@extend_schema_serializer(component_name="Vehicle Brand")
class VehicleBrandSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
    )

    class Meta:
        model = VehicleBrand
        fields = ("id", "name", "image_url")
        read_only_fields = ("id",)
