from rest_framework import serializers

from workshops.models import SpecialityModel


class WorkshopSpecialityListSerializer(serializers.ModelSerializer):
    speciality_id = serializers.PrimaryKeyRelatedField(
        source="speciality",
        queryset=SpecialityModel.objects.all(),
        write_only=True,
    )

    class Meta:
        model = SpecialityModel
        fields = ("speciality_id", "name")
        read_only_fields = ("name",)
