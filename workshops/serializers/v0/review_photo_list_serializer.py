from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import ReviewImage

from .review_photo_serializer import ReviewPhotoSerializer


class ReviewPhotoListSerializer(serializers.ListSerializer):
    child = ReviewPhotoSerializer()

    def validate_images(self, value):
        if len(value) > 5:
            raise serializers.ValidationError(
                _("You can only upload 5 images at a time")
            )

        return value

    def create(self, validated_data):
        images = {"images_url": []}
        review = self.context["review"]
        for image in validated_data["images"]:
            image = ReviewImage.objects.create(review=review, image=image)
            images["images_url"].append(image.image.url)
        return images
