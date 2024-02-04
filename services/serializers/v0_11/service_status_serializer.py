from rest_framework import serializers

from services.models import ServiceStatusModel


class ServiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStatusModel
        fields = ("id", "name")
