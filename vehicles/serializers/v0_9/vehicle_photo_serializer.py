from rest_framework import serializers

from vehicles.models import VehicleModel


class VehiclePhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(
        allow_empty_file=False,
        allow_null=False,
        required=True,
        source="image",
        use_url=True,
    )

    class Meta:
        model = VehicleModel
        fields = ("image_url",)
