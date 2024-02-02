from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty

from services.models import ServiceModel, ServiceStatusModel
from users.serializers.v0_9 import UserListSerializer
from vehicles.models import VehicleModel
from vehicles.serializers.v0_9 import VehicleSerializer


class PrivateServiceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(
        read_only=True,
        help_text=_("Vehicle data."),
    )
    requested_by = UserListSerializer(
        read_only=True,
        help_text=_("User data."),
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="services:detail",
        lookup_field="id",
        lookup_url_kwarg="service_id",
        help_text=_("URL to the service."),
    )

    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "number",
            "title",
            "description",
            "vehicle",
            "requested_by",
            "created_at",
            "closed_at",
            "url",
        )
        read_only_fields = (
            "id",
            "created_at",
            "closed_at",
        )

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["vehicle"] = serializers.CharField(write_only=True)

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["vehicle"] = VehicleSerializer()
        return validated_data

    def validate_vehicle(self, value):
        try:
            user = self.context["request"].user
            return user.vehicles.get(nickname__iexact=value)
        except VehicleModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Vehicle '{value}' does not exist.")
            )

    def create(self, validated_data):
        validated_data["workshop"] = self.context["workshop"]
        service = super().create(validated_data)
        service.histories.create(
            status=ServiceStatusModel.objects.get(name__iexact="Solicitado"),
            comment=service.description,
            responsable=self.context["request"].user,
        )
        return service
