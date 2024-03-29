from rest_framework import serializers

from core.fields.v0 import HyperLinkSelfField
from questions.models import Question
from users.serializers.v0 import UserListSerializer

from .question_response_serializer import QuestionResponseSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    answer = QuestionResponseSerializer(read_only=True, allow_null=True)
    workshop_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        source="workshop",
    )
    url = HyperLinkSelfField(
        view_name="workshops:question-detail",
        lookup_fields=("workshop_id", "number"),
        lookup_url_kwargs=("workshop_id", "question_number"),
    )

    class Meta:
        model = Question
        fields = (
            "id",
            "number",
            "body",
            "votes",
            "answer",
            "user",
            "created_at",
            "workshop_url",
            "url",
        )
        read_only_fields = ("id", "number", "votes", "created_at")

    def create(self, validated_data):
        validated_data["workshop"] = self.context["workshop"]
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
