from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields import StringRelatedHyperLinkField
from services.models import ServiceHistoryModel, ServiceStatusModel


class ServiceHistorySerializer(serializers.ModelSerializer):
    status = StringRelatedHyperLinkField(
        view_name="services:status-detail",
        read_only=True,
        lookup_field="id",
    )
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceStatusModel.objects.all(),
        write_only=True,
        source="status",
    )
    responsable = StringRelatedHyperLinkField(
        view_name="users:users-detail",
        read_only=True,
        lookup_field="id",
    )
    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        write_only=True,
        source="responsable",
    )

    class Meta:
        model = ServiceHistoryModel
        fields = (
            "id",
            "status",
            "status_id",
            "comment",
            "responsable",
            "responsable_id",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        service_id = self.context["service_id"]
        validated_data["service_id"] = service_id
        return super().create(validated_data)
