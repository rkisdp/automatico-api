from django.utils.translation import gettext_lazy as _
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
        # lookup_url_kwarg="vehicle_id",
        help_text=_("URL to the vehicle."),
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleModel.objects.all(),
        write_only=True,
        source="vehicle",
        help_text=_("The vehicle ID."),
    )
    requested_by = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
        help_text=_("URL to the user."),
    )
    url = HyperLinkSelfField(
        view_name="services:detail",
        lookup_field="id",
        # lookup_url_kwarg="service_id",
        help_text=_("URL to the service."),
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
