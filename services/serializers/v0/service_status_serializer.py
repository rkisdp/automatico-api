from rest_framework import serializers

from services.models import ServiceStatus


class ServiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStatus
        fields = ("id", "name")
