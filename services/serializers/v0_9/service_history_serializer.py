from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from services.models import (
    ServiceHistoryModel,
    ServiceModel,
    ServiceStatusModel,
)
from users.serializers.v0_9 import UserListSerializer


class ServiceHistorySerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField()
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceStatusModel.objects.all(),
        write_only=True,
        source="status",
    )
    responsable = UserListSerializer(read_only=True)
    responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        write_only=True,
        source="responsable",
        required=False,
        allow_null=True,
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

    def validate(self, attrs):
        status = attrs.get("status")
        service_id = self.context["service_id"]
        service = ServiceModel.objects.get(id=service_id)
        if (
            status
            and service.current_status_id in [4, 5, 7]
            and service.end_date
        ):
            raise serializers.ValidationError(
                {
                    "status_id": _(
                        "You can't change the status of a service that has "
                        "already been completed"
                    )
                }
            )

        responsable = attrs.get("responsable")
        if not responsable and status and status.id == 4:
            raise serializers.ValidationError(
                {
                    "responsable_id": _(
                        _("You must specify a responsible for this status")
                    )
                }
            )

        if (
            responsable
            and responsable not in service.workshop.employees.all()
            and responsable != service.workshop.owner
        ):
            raise serializers.ValidationError(
                {
                    "responsable_id": _(
                        "The responsible must be an employee or the owner "
                        "of the workshop"
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        service_id = self.context["service_id"]
        validated_data["service_id"] = service_id
        history = super().create(validated_data)
        service = history.service
        if history.status.id in [4, 5, 7]:
            service.end_date = timezone.now()
            service.save()

        if history.status.id in [5, 7]:
            history.responsable = self.context["request"].user
            history.save()

        if not service.response_description:
            service.response_description = history.comment
            service.save()

        return history
