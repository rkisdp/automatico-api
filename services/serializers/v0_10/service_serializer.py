from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from services.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="services:detail",
        lookup_field="id",
        lookup_url_kwarg="service_id",
        help_text=_("URL to the service."),
    )

    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "number",
            "title",
            "description",
            "created_at",
            "closed_at",
            "url",
        )
        read_only_fields = (
            "id",
            "number",
            "created_at",
            "closed_at",
        )
