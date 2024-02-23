from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopContact


class WorkshopContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopContact
        fields = (
            "id",
            "name",
            "value",
        )
        read_only_fields = ("id",)
