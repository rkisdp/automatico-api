from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import WorkshopModel


class WorkshopListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    employees_count = serializers.IntegerField(
        source="employees.count",
        read_only=True,
    )
    employees_url = HyperLinkSelfField(
        view_name="workshops:employees",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    brands_count = serializers.IntegerField(
        source="brands.count",
        read_only=True,
    )
    brands_url = HyperLinkSelfField(
        view_name="workshops:brands",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    specialities_count = serializers.IntegerField(
        source="specialities.count",
        read_only=True,
    )
    specialities_url = HyperLinkSelfField(
        view_name="workshops:specialities",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    vehicles_count = serializers.IntegerField(
        source="vehicles.count",
        read_only=True,
    )
    vehicles_url = HyperLinkSelfField(
        view_name="workshops:vehicles",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    url = HyperLinkSelfField(
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )

    class Meta:
        model = WorkshopModel
        fields = (
            "id",
            "owner",
            "name",
            "photo",
            "employees_count",
            "brands_count",
            "specialities_count",
            "vehicles_count",
            "employees_url",
            "brands_url",
            "specialities_url",
            "vehicles_url",
            "url",
        )
        read_only_fields = ("id", "photo")
