from services.models import ServiceStatusModel


from rest_framework import serializers


class ServiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStatusModel
        fields = ("id", "name")