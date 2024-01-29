from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty
from services.models import (
    ServiceHistoryModel,
    ServiceModel,
    ServiceStatusModel,
)
from users.serializers.v0_9 import UserListSerializer


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

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["responsable"] = serializers.EmailField(write_only=True)

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["responsable"] = UserListSerializer()
        return validated_data

    def validate_responsable(self, value):
        try:
            return get_user_model().objects.get(email__iexact=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError(
                _(f"User with responsable '{value}' does not exist.")
            )

    def validate_status(self, value):
        try:
            return ServiceStatusModel.objects.get(name__iexact=value)
        except ServiceStatusModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Service status '{value}' does not exist.")
            )

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
                    "responsable": _(
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
                    "responsable": _(
                        "The responsible must be an employee or the owner "
                        "of the workshop"
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        validated_data["service_id"] = self.context["service_id"]
        history = ServiceHistoryModel.objects.create(**validated_data)
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
