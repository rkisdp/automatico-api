from rest_framework import serializers

from vehicles.models import VehicleBrandModel, VehicleModel


class UserVehicleSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleBrandModel.objects.all(),
        source="brand",
        write_only=True,
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
            "image",
        )
        read_only_fields = ("id", "image")

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
