from rest_framework import serializers

from core.serializers import StringRelatedHyperLinkSerializer
from services.models import ServiceModel


class UserServiceSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="vehicle",
        queryset=ServiceModel.objects.all(),
    )
    workshop = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="workshops:detail",
        lookup_field="id",
    )
    workshop_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="workshop",
        queryset=ServiceModel.objects.all(),
    )
    current_status = StringRelatedHyperLinkSerializer(
        read_only=True,
        source="histories.last.status",
        view_name="services:status-detail",
        lookup_field="id",
        allow_null=True,
    )

    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "vehicle",
            "vehicle_id",
            "workshop",
            "workshop_id",
            "request_description",
            "response_description",
            "current_status",
            "start_date",
            "end_date",
        )
        read_only_fields = ("id", "start_date", "end_date")
