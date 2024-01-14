from rest_framework import serializers

from services.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = (
            "id",
            "vehicle",
            "workshop",
            "request_description",
            "response_description",
            "start_date",
            "end_date",
        )
        read_only_fields = ("id",)
