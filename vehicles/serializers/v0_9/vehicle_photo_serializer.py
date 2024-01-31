from rest_framework import serializers

from vehicles.models import VehicleModel


class VehiclePhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        write_only=True,
        allow_empty_file=False,
        allow_null=False,
        required=True,
        use_url=True,
    )
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
    )

    class Meta:
        model = VehicleModel
        fields = (
            "image",
            "image_url",
        )
