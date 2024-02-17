from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from services.models import ServiceHistoryModel, ServiceStatusModel
from users.serializers.v0 import UserListSerializer


class ServiceHistorySerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    responsable = UserListSerializer(read_only=True)

    class Meta:
        model = ServiceHistoryModel
        fields = (
            "id",
            "status",
            "comment",
            "responsable",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def validate_status(self, value):
        try:
            return ServiceStatusModel.objects.get(name__iexact=value)
        except ServiceStatusModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Service status '{value}' does not exist.")
            )

    def validate(self, attrs):
        status = attrs.get("status")
        service = self.context["service"]
        if (
            status
            and service.current_status_id in [4, 5, 7]
            and service.closed_at
        ):
            raise serializers.ValidationError(
                {
                    "status": _(
                        "You can't change the status of a service that has "
                        "already been completed."
                    )
                }
            )

        responsable = self.context["request"].user
        if (
            responsable not in service.workshop.employees.all()
            and responsable != service.workshop.owner
        ):
            raise serializers.ValidationError(
                {
                    "responsable": _(
                        "The responsible must be an employee or the owner "
                        "of the workshop."
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        validated_data["responsable"] = self.context["request"].user
        validated_data["service"] = self.context["service"]
        history = ServiceHistoryModel.objects.create(**validated_data)
        service = history.service
        if history.status.id in [4, 5, 7]:
            service.closed_at = timezone.now()
            service.save()

        if history.status.id in [5, 7]:
            history.responsable = self.context["request"].user
            history.save()

        return history
