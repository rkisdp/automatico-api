from rest_framework import serializers

from core.fields.v0_7 import StringRelatedHyperLinkField
from services.models import ServiceModel


class UserWorkshopServiceSerializer(serializers.ModelSerializer):
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
            "description",
            "current_status",
            "created_at",
            "closed_at",
        )
        read_only_fields = ("id",)
