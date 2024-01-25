from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import ReviewResponseModel


class ReviewResponseSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(view_name="workshops:review-responses")

    class Meta:
        model = ReviewResponseModel
        fields = (
            "id",
            "client",
            "workshop",
            "review",
            "response",
            "responded_at",
            "url",
        )
        read_only_fields = ("id", "responded_at")
