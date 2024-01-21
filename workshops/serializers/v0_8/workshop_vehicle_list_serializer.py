from rest_framework import serializers

from vehicles.models import VehicleModel


class WorkshopVehicleListSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(
        source="vehicle",
        queryset=VehicleModel.objects.all(),
        write_only=True,
    )

    class Meta:
        model = VehicleModel
        fields = (
            "vehicle_id",
            "brand",
            "model",
            "year",
            "nickname",
            "plate",
            "vin",
            "photo",
        )
        read_only_fields = (
            "brand",
            "model",
            "year",
            "nickname",
            "plate",
            "vin",
            "photo",
        )
