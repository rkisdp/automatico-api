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

    def create(self, validated_data):
        workshop = self.context["workshop"]
        for item in validated_data:
            workshop.contacts.update_or_create(
                name=item.get("name"),
                defaults={"value": item.get("value")},
            )
        return workshop.contacts.all()

    def update(self, instance, validated_data):
        contacts = []
        for item in validated_data:
            contact, _ = instance.contacts.update_or_create(
                name=item.get("name"),
                defaults={"value": item.get("value")},
            )
            contacts.append(contact)
        instance.contacts.exclude(
            id__in=(contact.id for contact in contacts)
        ).delete()
        return instance.contacts.all()
