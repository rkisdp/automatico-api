from rest_framework import serializers

from workshops.models import WorkshopContactModel


class WorkshopContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopContactModel
        fields = ("id", "workshop", "name", "value")
        read_only_fields = ("id",)
