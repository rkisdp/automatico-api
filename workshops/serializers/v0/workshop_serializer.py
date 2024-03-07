from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from workshops.models import Workshop


@extend_schema_serializer(component_name="Workshop")
class WorkshopSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField(
        help_text=_("Whether the workshop is a favorite of the user."),
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
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
        help_text=_("The image of the workshop."),
    )
    banner_url = serializers.ImageField(
        read_only=True,
        source="banner",
        use_url=True,
        help_text=_("The banner of the workshop."),
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
        model = Workshop
        fields = (
            "id",
            "name",
            "description",
            "rating",
            "recent_rating",
            "location",
            "is_favorite",
            "brands",
            "specialities",
            "brands_count",
            "specialities_count",
            "vehicles_count",
            "created_at",
            "image_url",
            "banner_url",
            "brands_url",
            "specialities_url",
            "vehicles_url",
            "url",
        )
        read_only_fields = ("id",)
        geo_field = "location"

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)

    def get_is_favorite(self, obj) -> bool:
        user = self.context["request"].user
        if user.is_anonymous:
            return False
        return user.favorite_workshops.filter(id=obj.id).exists()
