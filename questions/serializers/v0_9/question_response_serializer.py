from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from questions.models import QuestionResponseModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    client = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    question_url = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="questions:detail",
        lookup_field="id",
        lookup_url_kwarg="question_id",
    )
    url = HyperLinkSelfField(
        view_name="questions:response-detail",
        lookup_fields=("question_id", "id"),
        lookup_url_kwargs=("question_id", "response_id"),
    )

    class Meta:
        model = QuestionResponseModel
        fields = (
            "id",
            "body",
            "client",
            "question_url",
            "created_at",
            "url",
        )
        read_only_fields = ("id", "created_at")
