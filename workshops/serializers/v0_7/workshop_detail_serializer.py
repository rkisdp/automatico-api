from rest_framework import serializers

from core.serializers.v0_7 import StringRelatedHyperLinkSerializer
from workshops.models import WorkshopModel


class WorkshopDetailSerializer(serializers.ModelSerializer):
    owner = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    employees = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    brands = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
        lookup_url_kwarg="id",
    )
    specialities = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="workshops:speciality-detail",
        lookup_field="id",
        lookup_url_kwarg="speciality_id",
    )
    vehicles = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
        lookup_url_kwarg="id",
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
