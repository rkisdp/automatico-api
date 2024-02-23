from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from workshops.models import ReviewImage


class ReviewPhotoSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        write_only=True,
        child=serializers.ImageField(
            allow_empty_file=False,
            allow_null=False,
            required=False,
        ),
    )
    image_urls = serializers.ListField(
        read_only=True,
        child=serializers.ImageField(use_url=True),
    )

    class Meta:
        model = ReviewImage
        fields = (
            "images",
            "image_urls",
        )

    def validate_images(self, value):
        if len(value) > 5:
            raise serializers.ValidationError(
                _("You can only upload 5 images at a time")
            )

        return value

    def create(self, validated_data):
        images = []
        review = self.context["review"]
        for image in validated_data["images"]:
            image = ReviewImage.objects.create(
                review=review,
                image=image,
            )
            images.append(image.image)
        return {"image_urls": images}
