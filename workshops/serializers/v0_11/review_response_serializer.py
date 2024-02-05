from rest_framework import serializers

from users.serializers.v0_11 import UserListSerializer
from workshops.models import ReviewResponseModel


class ReviewResponseSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True, source="review.workshop.owner")
    workshop_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        source="review.workshop",
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    # review_url = serializers.HyperlinkedRelatedField(read_only=True)

    class Meta:
        model = ReviewResponseModel
        fields = (
            "id",
            "body",
            "user",
            "created_at",
            # "review_url",
            "workshop_url",
        )
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        validated_data["review"] = self.context["review"]
        return super().create(validated_data)
