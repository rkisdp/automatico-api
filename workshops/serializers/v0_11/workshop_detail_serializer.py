from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.serializers.v0_11 import UserListSerializer
from workshops.models import WorkshopModel


class WorkshopDetailSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(
        help_text=_("The account owner of the workshop."),
        read_only=True,
    )
    is_favorite = serializers.SerializerMethodField(
        help_text=_("Whether the workshop is a favorite of the user."),
    )
    brands_count = serializers.IntegerField(
        help_text=_("The count of brands of vehicles the workshop works with."),
        source="brands.count",
        read_only=True,
    )
    specialities_count = serializers.IntegerField(
        help_text=_("The count of specialities of the workshop."),
        source="specialities.count",
        read_only=True,
    )
    brands = serializers.ListSerializer(
        help_text=_("The brands of vehicles the workshop works with."),
        child=serializers.CharField(),
        read_only=True,
    )
    specialities = serializers.ListSerializer(
        help_text=_("The specialities of the workshop."),
        child=serializers.CharField(),
        read_only=True,
    )
    image_url = serializers.ImageField(
        help_text=_("The workshop image URL."),
        source="image",
        read_only=True,
        use_url=True,
    )
    url = serializers.HyperlinkedIdentityField(
        help_text=_("The workshop URL."),
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
            "rating",
            "recent_rating",
            "location",
            "is_favorite",
            "brands",
            "specialities",
            "brands_count",
            "specialities_count",
            "created_at",
            "image_url",
            "url",
        )
        read_only_fields = ("id",)
        geo_field = "location"

    def get_is_favorite(self, obj):
        user = self.context["request"].user
        if not user.is_authenticated:
            return False
        return user.favorite_workshops.filter(id=obj.id).exists()
