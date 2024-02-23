from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import Workshop

from .workshop_employee_list_serializer import WorkshopEmployeeListSerializer


class WorkshopEmployeeDetailSerializer(serializers.ListSerializer):
    child = WorkshopEmployeeListSerializer()

    def validate(self, attrs):
        emails = [item.get("email") for item in attrs]
        return self._clean_emails(emails)

    def create(self, validated_data):
        workshop = Workshop.objects.get(id=self.context.get("workshop_id"))
        for item in validated_data:
            employee = get_user_model().objects.get(
                email__iexact=item.get("email")
            )
            workshop.employees.add(employee)
        return workshop.employees.all()

    def update(self, instance: Workshop, validated_data):
        instance.employees.clear()
        for item in validated_data:
            employee = get_user_model().objects.get(
                email__iexact=item.get("email")
            )
            instance.employees.add(employee)
        return instance.employees.all()

    def _clean_emails(self, emails):
        cleaned_emails = []
        for email in emails:
            if email not in cleaned_emails:
                cleaned_emails.append({"email": email})
        return cleaned_emails
