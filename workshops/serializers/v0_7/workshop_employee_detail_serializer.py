from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopModel

from .workshop_employee_list_serializer import WorkshopEmployeeListSerializer


class WorkshopEmployeeDetailSerializer(serializers.ListSerializer):
    child = WorkshopEmployeeListSerializer()

    def validate(self, attrs):
        employees = [item.get("employee") for item in attrs]
        if len(employees) != len(set(employees)):
            raise serializers.ValidationError(
                {"employee_id": _("Employees cannot be duplicated")}
            )
        return attrs

    def update(self, instance: WorkshopModel, validated_data):
        instance.employees.clear()
        for item in validated_data:
            instance.employees.add(item.get("employee"))
        return instance.employees
