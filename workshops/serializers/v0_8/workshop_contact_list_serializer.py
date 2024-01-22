from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import WorkshopContactModel


class WorkshopContactListSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(
        view_name="workshops:contact-detail",
        lookup_field="id",
    )

    class Meta:
        model = WorkshopContactModel
        fields = (
            "id",
            "name",
            "value",
            "url",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        workshop_id = self.context.get("workshop_id")
        validated_data["workshop_id"] = workshop_id
        return super().create(validated_data)
