from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from questions.models import QuestionResponseModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(view_name="workshops:vehicle-list")

    class Meta:
        model = QuestionResponseModel
        fields = (
            "id",
            "client",
            "workshop",
            "question",
            "response",
            "responded_at",
            "url",
        )
        read_only_fields = ("id", "responded_at")
