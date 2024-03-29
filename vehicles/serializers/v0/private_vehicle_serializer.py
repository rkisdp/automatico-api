from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty

from users.serializers.v0 import UserListSerializer
from vehicles.models import Vehicle, VehicleBrand

from .vehicle_brand_serializer import VehicleBrandSerializer


class PrivateVehicleSerializer(serializers.ModelSerializer):
    brand = VehicleBrandSerializer(read_only=True)
    owner = UserListSerializer(read_only=True)
    imagen_url = serializers.ImageField(
        read_only=True,
        use_url=True,
        source="image",
    )

    class Meta:
        model = Vehicle
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "nickname",
            "owner",
            "plate",
            "vin",
            "is_archived",
            "imagen_url",
        )
        read_only_fields = ("id",)

    def get_fields(self):
        fields = super().get_fields()
        if self.context and self.context["request"].method != "GET":
            fields["brand"] = serializers.CharField(write_only=True)
        return fields

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["brand"] = VehicleBrandSerializer()
        return validated_data

    def validate_brand(self, value):
        try:
            return VehicleBrand.objects.get(name__iexact=value)
        except VehicleBrand.DoesNotExist:
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
