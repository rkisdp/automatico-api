from rest_framework import serializers

from workshops.models import ReviewResponseModel


class ReviewResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewResponseModel
        fields = (
            "id",
            "client",
            "workshop",
            "review",
            "response",
            "responded_at",
        )
        read_only_fields = ("id", "responded_at")
