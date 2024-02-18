from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from users.serializers.v0 import UserListSerializer
from workshops.models import WorkshopModel


@extend_schema_serializer(
    component_name="Workshop",
    deprecate_fields=("owner",),
)
class WorkshopSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(
        read_only=True,
        help_text=_("The account owner of the workshop."),
    )
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
            "brands_url",
            "specialities_url",
            "vehicles_url",
            "url",
        )
        read_only_fields = ("id",)
        geo_field = "location"

    def get_is_favorite(self, obj):
        user = self.context["request"].user
        if not user.is_authenticated:
            return False
        return user.favorite_workshops.filter(id=obj.id).exists()
