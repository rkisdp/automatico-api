from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty

from users.serializers.v0_9 import UserListSerializer
from vehicles.models import VehicleBrandModel, VehicleModel

from .vehicle_brand_serializer import VehicleBrandSerializer


class VehicleSerializer(serializers.ModelSerializer):
    brand = VehicleBrandSerializer(read_only=True)
    owner = UserListSerializer(read_only=True)
    imagen_url = serializers.ImageField(
        read_only=True,
        use_url=True,
        source="image",
    )

    class Meta:
        model = VehicleModel
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "owner",
            "plate",
            "vin",
            "imagen_url",
        )
        read_only_fields = ("id",)

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["brand"] = serializers.CharField(write_only=True)

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["brand"] = VehicleBrandSerializer()
        return validated_data

    def validate_brand(self, value):
        try:
            return VehicleBrandModel.objects.get(name__iexact=value)
        except VehicleBrandModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Vehicle brand '{value}' does not exist.")
            )

    def validate_nickname(self, value):
        user = self.context["request"].user
        vehicle_id = self.instance.id if self.instance else None
        if (
            user.vehicles.filter(nickname__iexact=value)
            .exclude(id=vehicle_id)
            .exists()
        ):
            raise serializers.ValidationError(
                _(f"Vehicle with nickname '{value}' already exists.")
            )

        return value

    def validate_plate(self, value):
        user = self.context["request"].user
        vehicle_id = self.instance.id if self.instance else None
        if (
            user.vehicles.filter(plate__iexact=value)
            .exclude(id=vehicle_id)
            .exists()
        ):
            raise serializers.ValidationError(
                _(f"Vehicle with plate '{value}' already exists.")
            )

        return value.upper()

    def validate_vin(self, value):
        user = self.context["request"].user
        vehicle_id = self.instance.id if self.instance else None
        if (
            user.vehicles.filter(vin__iexact=value)
            .exclude(id=vehicle_id)
            .exists()
        ):
            raise serializers.ValidationError(
                _(f"Vehicle with VIN '{value}' already exists.")
            )

        return value.upper()

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
