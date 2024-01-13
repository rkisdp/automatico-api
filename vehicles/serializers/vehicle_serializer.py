from rest_framework import serializers

from vehicles.models import VehicleModel


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "owner",
            "vin",
            "photo",
        )
        read_only_fields = ("id", "photo")
