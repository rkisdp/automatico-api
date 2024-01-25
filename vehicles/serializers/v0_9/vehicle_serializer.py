from rest_framework import serializers

from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from vehicles.models import VehicleModel


class VehicleSerializer(serializers.ModelSerializer):
    brand = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="vehicles:detail",
        lookup_field="id",
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
