from rest_framework import serializers

from vehicles.models import VehicleBrandModel


class VehicleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrandModel
        fields = ("id", "name")
        read_only_fields = ("id",)
