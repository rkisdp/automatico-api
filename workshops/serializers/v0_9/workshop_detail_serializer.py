from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from workshops.models import WorkshopModel


class WorkshopDetailSerializer(serializers.ModelSerializer):
    owner = StringRelatedHyperLinkSerializer(
        help_text=_("The account owner of the workshop."),
        read_only=True,
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    employees = StringRelatedHyperLinkSerializer(
        help_text=_("The workshop employees."),
        many=True,
        read_only=True,
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    brands = StringRelatedHyperLinkSerializer(
        help_text=_("The brands of vehicles the workshop works with."),
        many=True,
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
        lookup_url_kwarg="id",
    )
    specialities = StringRelatedHyperLinkSerializer(
        help_text=_("The specialities of the workshop."),
        many=True,
        read_only=True,
        view_name="workshops:speciality-detail",
        lookup_field="id",
        lookup_url_kwarg="speciality_id",
    )
    vehicles = StringRelatedHyperLinkSerializer(
        help_text=_("The vehicles the workshop currently has."),
        many=True,
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
        lookup_url_kwarg="id",
    )
    url = HyperLinkSelfField(
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
            "photo",
            "employees",
            "brands",
            "specialities",
            "vehicles",
            "url",
        )
        read_only_fields = ("id", "photo")
