from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from workshops.models import Workshop


@extend_schema_serializer(component_name="MinimalWorkshop")
class MinimalWorkshopSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField(
        help_text=_("Whether the workshop is a favorite of the user."),
    )
    brands = serializers.ListSerializer(
        child=serializers.CharField(),
        read_only=True,
        help_text=_("The brands of vehicles the workshop works with."),
    )
    specialities = serializers.ListSerializer(
        child=serializers.CharField(),
        read_only=True,
        help_text=_("The specialities of the workshop."),
    )
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
        help_text=_("The image of the workshop."),
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
            "rating",
            "is_favorite",
            "brands",
            "specialities",
            "created_at",
            "image_url",
            "url",
        )
        read_only_fields = ("id",)
        geo_field = "location"

    def get_is_favorite(self, obj) -> bool:
        user = self.context["request"].user
        if user.is_anonymous:
            return False
        return user.favorite_workshops.filter(id=obj.id).exists()
