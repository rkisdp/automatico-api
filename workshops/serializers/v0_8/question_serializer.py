from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from questions.models import QuestionModel


class QuestionSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(view_name="workshops:questions")

    class Meta:
        model = QuestionModel
        fields = (
            "id",
            "client",
            "workshop",
            "question",
            "questioned_at",
            "url",
        )
        read_only_fields = ("id", "questioned_at")
