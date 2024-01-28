from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from vehicles.models import VehicleBrandModel
from workshops.models import WorkshopModel

from .workshop_brand_list_serializer import WorkshopBrandListSerializer


class WorkshopBrandDetailSerializer(serializers.ListSerializer):
    child = WorkshopBrandListSerializer()

    def validate(self, attrs):
        brands = [item.get("name") for item in attrs]
        return self._clean_brands(brands)

    def create(self, validated_data):
        workshop = WorkshopModel.objects.get(id=self.context.get("workshop_id"))
        for item in validated_data:
            try:
                brand = VehicleBrandModel.objects.get(
                    name__iexact=item.get("name")
                )
            except VehicleBrandModel.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "name": _(
                            f"The brand '{item.get('name')}' does not exist."
                        )
                    }
                )
            workshop.brands.add(brand)
        return workshop.brands.all()

    def update(self, instance: WorkshopModel, validated_data):
        instance.brands.clear()
        for item in validated_data:
            try:
                brand = VehicleBrandModel.objects.get(
                    name__iexact=item.get("name")
                )
            except VehicleBrandModel.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "name": _(
                            f"The brand '{item.get('name')}' does not exist."
                        )
                    }
                )
            instance.brands.add(brand)
        return instance.brands.all()

    def _clean_brands(self, brands):
        cleaned_brands = []
        for brand in brands:
            if brand not in cleaned_brands:
                cleaned_brands.append({"name": brand})
        return cleaned_brands
