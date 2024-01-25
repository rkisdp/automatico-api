from rest_framework import serializers

from vehicles.models import VehicleModel


class VehiclePhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        allow_empty_file=False,
        allow_null=False,
        required=True,
        use_url=True,
    )

    class Meta:
        model = VehicleModel
        fields = ("photo",)
