from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import WorkshopModel


class WorkshopBannerSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(
        write_only=True,
        allow_empty_file=False,
        allow_null=False,
        required=True,
    )
    banner_url = serializers.ImageField(
        use_url=True,
        read_only=True,
        source="banner",
    )

    class Meta:
        model = WorkshopModel
        fields = (
            "banner",
            "banner_url",
        )
