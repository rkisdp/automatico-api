from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from vehicles.models import VehicleBrandModel


@extend_schema_serializer(component_name="Vehicle Brand")
class VehicleBrandSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="vehicles:brand-detail",
        lookup_field="id",
        lookup_url_kwarg="brand_id",
    )

    class Meta:
        model = VehicleBrandModel
        fields = ("id", "name", "image_url", "url")
        read_only_fields = ("id",)
