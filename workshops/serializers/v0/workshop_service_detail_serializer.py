from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import Workshop

from .workshop_service_list_serializer import WorkshopServiceListSerializer


class WorkshopServiceDetailSerializer(serializers.ListSerializer):
    child = WorkshopServiceListSerializer()

    def validate(self, attrs):
        services = [item.get("service") for item in attrs]
        if len(services) != len(set(services)):
            raise serializers.ValidationError(
                {"id": _("Specialities cannot be duplicated")}
            )
        return attrs

    def update(self, instance: Workshop, validated_data):
        instance.services.clear()
        for item in validated_data:
            instance.services.add(item.get("service"))
        return instance.services
