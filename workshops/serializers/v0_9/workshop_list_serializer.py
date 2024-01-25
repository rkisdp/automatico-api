from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import WorkshopModel


class WorkshopListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(
        read_only=True,
        help_text=_("The account owner of the workshop."),
    )
    employees_count = serializers.IntegerField(
        source="employees.count",
        read_only=True,
        help_text=_("Number of employees in the workshop."),
    )
    employees_url = HyperLinkSelfField(
        view_name="workshops:employees",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of employees in the workshop."),
    )
    brands_count = serializers.IntegerField(
        source="brands.count",
        read_only=True,
        help_text=_("Number of brands in the workshop."),
    )
    brands_url = HyperLinkSelfField(
        view_name="workshops:brands",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of brands in the workshop."),
    )
    specialities_count = serializers.IntegerField(
        source="specialities.count",
        read_only=True,
        help_text=_("Number of specialities in the workshop."),
    )
    specialities_url = HyperLinkSelfField(
        view_name="workshops:specialities",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of specialities in the workshop."),
    )
    vehicles_count = serializers.IntegerField(
        source="vehicles.count",
        read_only=True,
        help_text=_("Number of vehicles in the workshop."),
    )
    vehicles_url = HyperLinkSelfField(
        view_name="workshops:vehicles",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of vehicles in the workshop."),
    )
    url = HyperLinkSelfField(
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the workshop."),
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

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return super().create(validated_data)
