from rest_framework import serializers

from core.serializers import StringRelatedHyperLinkSerializer
from services.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkSerializer(
        view_name="vehicles:detail", read_only=True, lookup_field="id"
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        source="vehicle", queryset=ServiceModel.objects.all(), write_only=True
    )
    requested_by = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    workshop = StringRelatedHyperLinkSerializer(
        view_name="workshops:detail", read_only=True, lookup_field="id"
    )
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop", queryset=ServiceModel.objects.all(), write_only=True
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
        )
        read_only_fields = ("id",)
