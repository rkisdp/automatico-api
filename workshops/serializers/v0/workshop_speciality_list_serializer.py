from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from workshops.models import Speciality


class WorkshopSpecialityListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    url = HyperLinkSelfField(
        view_name="workshops:specialities",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )

    class Meta:
        model = Speciality
        fields = ("id", "name", "url")
