from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import SpecialityModel


class WorkshopSpecialityListSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(
        view_name="workshops:speciality-detail",
        lookup_field="id",
    )

    class Meta:
        model = SpecialityModel
        fields = (
            "id",
            "name",
            "url",
        )
        read_only_fields = ("name",)
