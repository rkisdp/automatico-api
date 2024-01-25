from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from vehicles.models import VehicleModel


class WorkshopVehicleListSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="vehicle",
        queryset=VehicleModel.objects.all(),
    )
    brand = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = HyperLinkSelfField(view_name="vehicles:detail", lookup_field="id")

    class Meta:
        model = VehicleModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "plate",
            "vin",
            "photo",
            "url",
        )
        read_only_fields = (
            "brand",
            "model",
            "year",
            "nickname",
            "plate",
            "vin",
        )
