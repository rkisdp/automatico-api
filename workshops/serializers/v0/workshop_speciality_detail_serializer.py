from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import Speciality, Workshop

from .workshop_speciality_list_serializer import (
    WorkshopSpecialityListSerializer,
)


class WorkshopSpecialityDetailSerializer(serializers.ListSerializer):
    child = WorkshopSpecialityListSerializer()

    def validate(self, attrs):
        specialities = [item.get("name") for item in attrs]
        return self._clean_specialities(specialities)

    def create(self, validated_data):
        workshop = self.context["workshop"]
        for item in validated_data:
            try:
                speciality = Speciality.objects.get(
                    name__iexact=item.get("name")
                )
            except Speciality.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "name": _(
                            f"Speciality '{item.get('name')}' does not exists."
                        )
                    }
                )
            workshop.specialities.add(speciality)
        return workshop.specialities.all()

    def update(self, instance: Workshop, validated_data):
        instance.specialities.clear()
        for item in validated_data:
            try:
                speciality = Speciality.objects.get(
                    name__iexact=item.get("name")
                )
            except Speciality.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "name": _(
                            f"Speciality '{item.get('name')}' does not exists."
                        )
                    }
                )
            instance.specialities.add(speciality)
        return instance.specialities.all()

    def _clean_specialities(self, specialities):
        cleaned_specialities = []
        for speciality in specialities:
            if speciality not in cleaned_specialities:
                cleaned_specialities.append({"name": speciality})
        return cleaned_specialities
