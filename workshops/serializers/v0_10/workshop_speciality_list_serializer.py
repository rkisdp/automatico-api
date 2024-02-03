from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import SpecialityModel


class WorkshopSpecialityListSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(
        view_name="workshops:specialities",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )

    class Meta:
        model = SpecialityModel
        fields = ("id", "name", "url")
