from rest_framework import serializers

from workshops.models import WorkshopContactModel


class WorkshopContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopContactModel
        fields = ("name", "value")

    def create(self, validated_data):
        workshop_id = self.context.get("workshop_id")
        validated_data["workshop_id"] = workshop_id
        return super().create(validated_data)
