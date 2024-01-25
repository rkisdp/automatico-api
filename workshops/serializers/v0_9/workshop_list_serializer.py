from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from core.fields.v0_9 import HyperLinkSelfField
from users.serializers.v0_9 import UserListSerializer
from workshops.models import WorkshopModel


@extend_schema_serializer(component_name="Workshop List")
class WorkshopListSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(
        read_only=True,
        help_text=_("The account owner of the workshop."),
    )
    brands = serializers.ListSerializer(
        child=serializers.CharField(),
        read_only=True,
        help_text=_("The brands of vehicles the workshop works with."),
    )
    brands_count = serializers.IntegerField(
        source="brands.count",
        read_only=True,
        help_text=_("Number of brands in the workshop."),
    )
    specialities_count = serializers.IntegerField(
        source="specialities.count",
        read_only=True,
        help_text=_("Number of specialities in the workshop."),
    )
    specialities = serializers.ListSerializer(
        child=serializers.CharField(),
        read_only=True,
        help_text=_("The specialities of the workshop."),
    )
    vehicles_count = serializers.IntegerField(
        source="vehicles.count",
        read_only=True,
        help_text=_("Number of vehicles in the workshop."),
    )
    brands_url = HyperLinkSelfField(
        view_name="workshops:brands",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of brands in the workshop."),
    )
    specialities_url = HyperLinkSelfField(
        view_name="workshops:specialities",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        help_text=_("URL to the list of specialities in the workshop."),
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
            "brands",
            "specialities",
            "brands_count",
            "specialities_count",
            "vehicles_count",
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
