from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopModel

from .workshop_speciality_list_serializer import (
    WorkshopSpecialityListSerializer,
)


class WorkshopSpecialityDetailSerializer(serializers.ListSerializer):
    child = WorkshopSpecialityListSerializer()

    def validate(self, attrs):
        specialities = [item.get("speciality") for item in attrs]
        if len(specialities) != len(set(specialities)):
            raise serializers.ValidationError(
                {"speciality_id": _("Specialities cannot be duplicated")}
            )
        return attrs

    def update(self, instance: WorkshopModel, validated_data):
        instance.specialities.clear()
        for item in validated_data:
            instance.specialities.add(item.get("speciality"))
        return instance.specialities
