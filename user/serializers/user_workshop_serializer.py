from rest_framework import serializers

from core.fields import StringRelatedHyperLinkField
from workshops.models import WorkshopModel


class UserWorkshopSerializer(serializers.ModelSerializer):
    owner = StringRelatedHyperLinkField(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    name = serializers.CharField(
        max_length=100,
        validators=[WorkshopModel.validate_unique_name],
        trim_whitespace=True,
    )
    employees = StringRelatedHyperLinkField(
        many=True,
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    brands = StringRelatedHyperLinkField(
        many=True,
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    specialities = StringRelatedHyperLinkField(
        many=True,
        read_only=True,
        view_name="workshops:speciality-detail",
        lookup_field="id",
    )
    vehicles = StringRelatedHyperLinkField(
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
            "photo",
            "employees",
            "brands",
            "specialities",
            "vehicles",
        )
        read_only_fields = ("id", "photo")

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
