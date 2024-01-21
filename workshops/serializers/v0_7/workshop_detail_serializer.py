from rest_framework import serializers

from core.serializers import StringRelatedHyperLinkSerializer
from workshops.models import WorkshopModel


class WorkshopDetailSerializer(serializers.ModelSerializer):
    owner = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    employees = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    brands = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    specialities = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="workshops:speciality-detail",
        lookup_field="id",
    )
    vehicles = StringRelatedHyperLinkSerializer(
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
            "photo",
            "employees",
            "brands",
            "specialities",
            "vehicles",
        )
        read_only_fields = ("id", "photo")
