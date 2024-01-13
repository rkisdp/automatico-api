from rest_framework import serializers

from workshops.models import WorkshopModel


class WorkshopSerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    specialities = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="workshops:specialities-detail",
        lookup_field="id",
    )
    vehicles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="vehicles:detail",
        lookup_field="id",
    )

    class Meta:
        model = WorkshopModel
        fields = (
            "id",
            "owner",
            "name",
            "latitude",
            "longitude",
            "employees",
            "specialities",
            "vehicles",
        )
        read_only_fields = ("id",)
