from rest_framework import serializers

from workshops.models import ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ("id", "workshop")
        read_only_fields = ("id",)
