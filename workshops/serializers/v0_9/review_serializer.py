from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(view_name="workshops:reviews")

    class Meta:
        model = ReviewModel
        fields = (
            "id",
            "workshop",
            "service",
            "client",
            "review",
            "score",
            "reviewed_at",
            "url",
        )
        read_only_fields = ("id", "reviewed_at")
