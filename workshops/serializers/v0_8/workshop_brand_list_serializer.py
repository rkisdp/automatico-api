from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from vehicles.models import VehicleBrandModel


class WorkshopBrandListSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )

    class Meta:
        model = VehicleBrandModel
        fields = (
            "id",
            "name",
            "url",
        )
        read_only_fields = ("name",)
