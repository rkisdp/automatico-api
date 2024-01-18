from rest_framework import serializers

from core.fields import StringRelatedHyperLinkField
from services.models import ServiceModel, ServiceStatusModel
from vehicles.models import VehicleModel


class WorkshopServiceListSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkField(
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleModel.objects.all(),
        write_only=True,
        source="vehicle",
    )
    requested_by = StringRelatedHyperLinkField(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )

    class Meta:
        model = ServiceModel
        fields = (
            "vehicle",
            "vehicle_id",
            "requested_by",
            "request_description",
            "response_description",
            "start_date",
            "end_date",
        )
        read_only_fields = ("response_description", "start_date", "end_date")

    def create(self, validated_data):
        service = super().create(validated_data)
        user = self.context["request"].user
        service.histories.create(
            status=ServiceStatusModel.objects.get(name="Solicitado"),
            responsable=user,
        )
        return service
