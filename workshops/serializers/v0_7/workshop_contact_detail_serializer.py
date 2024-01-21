from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopContactModel

from .workshop_contact_list_serializer import WorkshopContactListSerializer


class WorkshopContactDetailSerializer(serializers.ListSerializer):
    child = WorkshopContactListSerializer()

    def validate(self, attrs):
        names = [item.get("name") for item in attrs]
        if len(names) != len(set(names)):
            raise serializers.ValidationError(
                {"name": _("Name must be unique.")}
            )
        return attrs

    def update(self, instance, validated_data):
        workshop_id = self.context.get("workshop_id")
        WorkshopContactModel.objects.filter(workshop_id=workshop_id).delete()
        contacts = []
        for item in validated_data:
            instance, created = WorkshopContactModel.objects.update_or_create(
                name=item.get("name"),
                defaults={
                    "value": item.get("value"),
                    "workshop_id": workshop_id,
                },
            )
            contacts.append(instance)
        return contacts
