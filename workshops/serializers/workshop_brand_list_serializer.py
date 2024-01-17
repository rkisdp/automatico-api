from rest_framework import serializers

from vehicles.models import VehicleBrandModel


class WorkshopBrandListSerializer(serializers.ModelSerializer):
    brand_id = serializers.PrimaryKeyRelatedField(
        source="brand",
        queryset=VehicleBrandModel.objects.all(),
        write_only=True,
    )

    class Meta:
        model = VehicleBrandModel
        fields = ("brand_id", "name")
        read_only_fields = ("name",)
