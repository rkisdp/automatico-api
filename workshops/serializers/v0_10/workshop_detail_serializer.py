from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.serializers.v0_9 import UserListSerializer
from workshops.models import WorkshopModel


class WorkshopDetailSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(
        help_text=_("The account owner of the workshop."),
        read_only=True,
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
            "name",
            "owner",
            "brands",
            "specialities",
            "brands_count",
            "specialities_count",
            "image_url",
            "url",
        )
        read_only_fields = ("id",)
