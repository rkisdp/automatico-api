from rest_framework import serializers

from workshops.models import SpecialityModel


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityModel
        fields = ("id", "name")
        read_only_fields = ("id", "name")
