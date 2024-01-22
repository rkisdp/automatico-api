from rest_framework import serializers

from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from services.models import ServiceModel


class UserWorkshopServiceSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkSerializer(
        view_name="vehicles:detail",
        read_only=True,
        lookup_field="id",
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        source="vehicle",
        queryset=ServiceModel.objects.all(),
        write_only=True,
    )
    workshop = StringRelatedHyperLinkSerializer(
        view_name="workshops:detail",
        read_only=True,
        lookup_field="id",
    )
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop",
        queryset=ServiceModel.objects.all(),
        write_only=True,
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
        read_only_fields = ("id",)
