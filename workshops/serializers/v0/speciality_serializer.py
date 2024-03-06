from rest_framework import serializers

from workshops.models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        read_only=True,
        use_url=True,
        source="image",
    )

    class Meta:
        model = Speciality
        fields = ("id", "name", "image_url")
        read_only_fields = ("id", "name")
