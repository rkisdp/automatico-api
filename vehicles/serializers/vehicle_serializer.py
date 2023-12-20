from rest_framework import serializers

from vehicles.models import VehicleBrandModel, VehicleModel


class VehicleBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrandModel
        fields = ("id", "name")
        read_only_fields = ("id",)


class VehicleModelSerializer(serializers.ModelSerializer):
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
        read_only_fields = ("id",)


class VehicleBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrandModel
        fields = ("id", "name")
        read_only_fields = ("id",)
