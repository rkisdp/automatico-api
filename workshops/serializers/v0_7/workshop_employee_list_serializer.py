from django.contrib.auth import get_user_model
from rest_framework import serializers


class WorkshopEmployeeListSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(
        source="employee",
        queryset=get_user_model().objects.all(),
        write_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "photo",
            "phone_number",
        )
        read_only_fields = (
            "first_name",
            "last_name",
            "email",
            "photo",
            "phone_number",
        )
