from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty

from users.serializers.v0_9 import UserListSerializer
from vehicles.models import VehicleBrandModel, VehicleModel

from .vehicle_brand_serializer import VehicleBrandSerializer


class VehicleSerializer(serializers.ModelSerializer):
    brand = VehicleBrandSerializer(read_only=True)
    imagen_url = serializers.ImageField(
        read_only=True,
        use_url=True,
        source="image",
    )
    owner = UserListSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="vehicles:detail",
        lookup_field="id",
        lookup_url_kwarg="vehicle_id",
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
            "url",
        )
        read_only_fields = ("id",)

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["brand"] = serializers.CharField(write_only=True)
        if data is not empty:
            data["brand"] = {"name": data.get("brand", None)}
            self.fields["brand"] = VehicleBrandSerializer()

    def validate_brand(self, value):
        name = value.get("name", None)
        try:
            return VehicleBrandModel.objects.get(name__iexact=name)
        except VehicleBrandModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Vehicle brand '{name}' does not exist.")
            )

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
