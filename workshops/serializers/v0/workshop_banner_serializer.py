from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import ReviewImageModel


class WorkshopBannerSerializer(serializers.ModelSerializer):
    banner = serializers.ListField(
        write_only=True,
        child=serializers.ImageField(
            allow_empty_file=False,
            allow_null=False,
            required=False,
        ),
    )
    banner_url = serializers.ListField(
        read_only=True,
        child=serializers.ImageField(use_url=True),
    )

    class Meta:
        model = ReviewImageModel
        fields = (
            "banner",
            "banner_url",
        )
