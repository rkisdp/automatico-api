from rest_framework import serializers

from vehicles.models import VehicleModel

from .vehicle_brand_serializer import VehicleBrandSerializer


class VehicleSerializer(serializers.ModelSerializer):
    brand = VehicleBrandSerializer(read_only=True)
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="vehicles:detail",
        lookup_field="id",
        lookup_url_kwarg="vehicle_id",
    )

    class Meta:
        model = VehicleModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "owner",
            "plate",
            "vin",
            "photo",
            "url",
        )
        read_only_fields = ("id",)
