from rest_framework import serializers

from workshops.models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ("id", "name")
        read_only_fields = ("id", "name")
