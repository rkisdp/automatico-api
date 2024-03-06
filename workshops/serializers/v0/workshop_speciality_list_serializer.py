from rest_framework import serializers

from workshops.models import Speciality


class WorkshopSpecialityListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    image_url = serializers.ImageField(
        read_only=True,
        use_url=True,
        source="image",
    )

    class Meta:
        model = Speciality
        fields = ("id", "name", "image_url")
