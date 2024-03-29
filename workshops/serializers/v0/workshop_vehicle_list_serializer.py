from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from core.serializers.v0 import StringRelatedHyperLinkSerializer
from vehicles.models import Vehicle


class WorkshopVehicleListSerializer(serializers.ModelSerializer):
    brand = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
        lookup_url_kwarg="brand_id",
    )
    image = serializers.ImageField(read_only=True, use_url=True)
    url = HyperLinkSelfField(
        view_name="vehicles:detail",
        lookup_field="id",
        lookup_url_kwarg="vehicle_id",
    )

    class Meta:
        model = Vehicle
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "plate",
            "vin",
            "image",
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
