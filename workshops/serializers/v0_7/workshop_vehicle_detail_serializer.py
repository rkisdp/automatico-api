from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopModel

from .workshop_vehicle_list_serializer import WorkshopVehicleListSerializer


class WorkshopVehicleDetailSerializer(serializers.ListSerializer):
    child = WorkshopVehicleListSerializer()

    def validate(self, attrs):
        vehicles = [item.get("vehicle") for item in attrs]
        if len(vehicles) != len(set(vehicles)):
            raise serializers.ValidationError(
                {"vehicle_id": _("Specialities cannot be duplicated")}
            )
        return attrs

    def update(self, instance: WorkshopModel, validated_data):
        instance.vehicles.clear()
        for item in validated_data:
            instance.vehicles.add(item.get("vehicle"))
        return instance.vehicles
