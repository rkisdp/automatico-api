from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.fields import empty

from core.fields.v0_8 import HyperLinkSelfField
from vehicles.models import VehicleBrandModel


class WorkshopBrandListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text=_("Name of the vehicle brand."))
    url = HyperLinkSelfField(
        view_name="vehicles:brand-detail",
        lookup_field="id",
        help_text=_("URL to the vehicle brand."),
    )

    class Meta:
        model = VehicleBrandModel
        fields = (
            "id",
            "name",
            "url",
        )
        read_only_fields = ("id",)
