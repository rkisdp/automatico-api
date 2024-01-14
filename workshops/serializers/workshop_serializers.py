from rest_framework import serializers

from core.fields import HyperLinkStringRelatedField
from workshops.models import WorkshopModel


class WorkshopSerializer(serializers.ModelSerializer):
    owner = HyperLinkStringRelatedField(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    employees = HyperLinkStringRelatedField(
        many=True,
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    specialities = HyperLinkStringRelatedField(
        many=True,
        read_only=True,
        view_name="workshops:specialities-detail",
        lookup_field="id",
    )
    vehicles = HyperLinkStringRelatedField(
        many=True,
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
    )

    class Meta:
        model = WorkshopModel
        fields = (
            "id",
            "owner",
            "name",
            "latitude",
            "longitude",
            "employees",
            "specialities",
            "vehicles",
        )
        read_only_fields = ("id",)
