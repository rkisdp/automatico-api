from rest_framework import serializers

from workshops.models import ReviewPhotoModel


class ReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPhotoModel
        fields = ("id", "review", "photo")
        read_only_fields = ("id",)
