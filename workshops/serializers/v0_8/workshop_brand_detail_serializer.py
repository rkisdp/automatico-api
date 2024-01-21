from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopModel

from .workshop_brand_list_serializer import WorkshopBrandListSerializer


class WorkshopBrandDetailSerializer(serializers.ListSerializer):
    child = WorkshopBrandListSerializer()

    def validate(self, attrs):
        brands = [item.get("brand") for item in attrs]
        if len(brands) != len(set(brands)):
            raise serializers.ValidationError(
                {"brand": _("Brands cannot be duplicated")}
            )
        return attrs

    def update(self, instance: WorkshopModel, validated_data):
        instance.brands.clear()
        for item in validated_data:
            instance.brands.add(item.get("brand"))
        return instance.brands
