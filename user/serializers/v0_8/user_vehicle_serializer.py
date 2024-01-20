from rest_framework import serializers

from core.serializers import StringRelatedHyperLinkSerializer
from vehicles.models import VehicleBrandModel, VehicleModel


class UserVehicleSerializer(serializers.ModelSerializer):
    brand = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    brand_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="brand",
        queryset=VehicleBrandModel.objects.all(),
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
            "brand_id",
            "model",
            "year",
            "nickname",
            "vin",
            "photo",
            "url",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
