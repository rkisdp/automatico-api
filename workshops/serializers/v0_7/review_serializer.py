from rest_framework import serializers

from workshops.models import ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
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
        )
        read_only_fields = ("id", "reviewed_at")
