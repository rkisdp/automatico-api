from rest_framework import serializers

from vehicles.models import VehicleBrandModel


class VehicleBrandSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )

    class Meta:
        model = VehicleBrandModel
        fields = ("id", "name", "url")
        read_only_fields = ("id",)
