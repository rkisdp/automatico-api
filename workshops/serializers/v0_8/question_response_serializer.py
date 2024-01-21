from rest_framework import serializers

from workshops.models import QuestionResponseModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponseModel
        fields = (
            "id",
            "client",
            "workshop",
            "question",
            "response",
            "responded_at",
        )
        read_only_fields = ("id", "responded_at")
