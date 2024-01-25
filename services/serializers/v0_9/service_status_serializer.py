from rest_framework import serializers

from services.models import ServiceStatusModel


class ServiceStatusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="services:status-detail",
        lookup_field="id",
        lookup_url_kwarg="status_id",
    )

    class Meta:
        model = ServiceStatusModel
        fields = (
            "id",
            "name",
            "url",
        )
