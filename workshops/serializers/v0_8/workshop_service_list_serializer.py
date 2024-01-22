from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from services.models import ServiceModel, ServiceStatusModel
from vehicles.models import VehicleModel


class WorkshopServiceListSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleModel.objects.all(),
        write_only=True,
        source="vehicle",
    )
    requested_by = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    url = HyperLinkSelfField(
        view_name="services:detail",
        lookup_field="id",
    )

    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "vehicle",
            "vehicle_id",
            "requested_by",
            "request_description",
            "response_description",
            "start_date",
            "end_date",
            "url",
        )
        read_only_fields = (
            "id",
            "response_description",
            "start_date",
            "end_date",
        )

    def create(self, validated_data):
        workshop_id = self.context["workshop_id"]
        validated_data["workshop_id"] = workshop_id
        service = super().create(validated_data)
        service.histories.create(
            status=ServiceStatusModel.objects.get(name="Solicitado"),
            comment=service.request_description,
            responsable=self.context["request"].user,
        )
        return service
