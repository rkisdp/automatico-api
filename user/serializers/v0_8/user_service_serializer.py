from rest_framework import serializers

from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
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
    url = serializers.HyperlinkedIdentityField(
        view_name="services:detail",
        lookup_field="id",
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
            "url",
        )
        read_only_fields = ("id", "created_at", "closed_at")
