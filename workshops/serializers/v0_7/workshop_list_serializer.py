from django.contrib.auth import get_user_model
from rest_framework import serializers

from workshops.models import WorkshopModel


class WorkshopListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        source="owner",
        queryset=get_user_model().objects.all(),
        write_only=True,
    )
    employees_count = serializers.IntegerField(
        source="employees.count", read_only=True
    )
    brands_count = serializers.IntegerField(
        source="brands.count", read_only=True
    )
    specialities_count = serializers.IntegerField(
        source="specialities.count", read_only=True
    )
    vehicles_count = serializers.IntegerField(
        source="vehicles.count", read_only=True
    )

    class Meta:
        model = WorkshopModel
        fields = (
            "id",
            "owner",
            "owner_id",
            "name",
            "photo",
            "employees_count",
            "brands_count",
            "specialities_count",
            "vehicles_count",
        )
        read_only_fields = ("id", "photo")
