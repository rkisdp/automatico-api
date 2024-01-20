from rest_framework import serializers

from core.serializers import StringRelatedHyperLinkSerializer
from workshops.models import WorkshopModel


class UserWorkshopSerializer(serializers.ModelSerializer):
    owner = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    name = serializers.CharField(
        max_length=100,
        validators=[WorkshopModel.validate_unique_name],
        trim_whitespace=True,
    )
    employees = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
    )
    brands = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="vehicles:brand-detail",
        lookup_field="id",
    )
    specialities = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        view_name="workshops:speciality-detail",
        lookup_field="id",
    )
    vehicles = StringRelatedHyperLinkSerializer(
        many=True,
        read_only=True,
        lookup_field="id",
        view_name="vehicles:detail",
    )
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="workshops:detail",
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
            "url",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
