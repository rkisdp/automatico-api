from rest_framework import serializers

from services.models import ServiceModel
from users.serializers.v0_9 import UserListSerializer
from vehicles.serializers.v0_9 import VehicleSerializer
from workshops.serializers.v0_9 import WorkshopListSerializer


class ServiceSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(
        source="vehicle",
        queryset=ServiceModel.objects.all(),
        write_only=True,
    )
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop",
        queryset=ServiceModel.objects.all(),
        write_only=True,
    )
    vehicle = VehicleSerializer(read_only=True)
    requested_by = UserListSerializer(read_only=True)
    workshop = WorkshopListSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="services:detail",
        lookup_field="id",
        lookup_url_kwarg="service_id",
    )

    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "vehicle",
            "vehicle_id",
            "requested_by",
            "workshop",
            "workshop_id",
            "request_description",
            "response_description",
            "current_status",
            "start_date",
            "end_date",
            "url",
        )
        read_only_fields = ("id",)
