from rest_framework import serializers

from workshops.models import ReviewResponseModel


class ReviewResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewResponseModel
        fields = ("id", "review", "response")
        read_only_fields = ("id",)
