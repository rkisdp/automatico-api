from rest_framework import serializers

from services.models import (
    ServiceHistoryModel,
    ServiceModel,
    ServiceStatusModel,
)


class ServiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStatusModel
        fields = ("id", "name")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ("id",)
        read_only_fields = ("id",)


class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistoryModel
        fields = ("id",)
        read_only_fields = ("id",)
