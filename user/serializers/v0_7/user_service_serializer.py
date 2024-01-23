from rest_framework import serializers

from core.fields.v0_7 import StringRelatedHyperLinkField
from services.models import ServiceModel


class UserServiceSerializer(serializers.ModelSerializer):
    vehicle = StringRelatedHyperLinkField(
        view_name="vehicles:detail", read_only=True, lookup_field="id"
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        source="vehicle", queryset=ServiceModel.objects.all(), write_only=True
    )
    workshop = StringRelatedHyperLinkField(
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
            "workshop",
            "workshop_id",
            "request_description",
            "response_description",
            "current_status",
            "start_date",
            "end_date",
        )
        read_only_fields = ("id",)
