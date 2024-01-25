from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import ReviewPhotoModel


class ReviewPhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(read_only=True, use_url=True)
    url = HyperLinkSelfField(view_name="workshops:review-photos")

    class Meta:
        model = ReviewPhotoModel
        fields = (
            "id",
            "review",
            "photo",
            "url",
        )
        read_only_fields = ("id",)
