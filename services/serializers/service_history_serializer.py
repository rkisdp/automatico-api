from rest_framework import serializers

from services.models import ServiceHistoryModel


class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistoryModel
        fields = ("id",)
        read_only_fields = ("id",)
