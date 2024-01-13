from rest_framework import serializers

from services.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ("id",)
        read_only_fields = ("id",)
