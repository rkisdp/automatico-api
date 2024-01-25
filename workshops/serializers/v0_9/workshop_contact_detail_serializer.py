from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

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
        for item in validated_data:
            instance.contacts.update_or_create(
                name=item.get("name"),
                defaults={"value": item.get("value")},
            )
        return instance.contacts.all()
