from rest_framework import serializers

from questions.models import QuestionModel
from users.serializers.v0_9 import UserListSerializer

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

    class Meta:
        model = QuestionModel
        fields = (
            "id",
            "number",
            "body",
            "votes",
            "answer",
            "user",
            "created_at",
            "workshop_url",
        )
        read_only_fields = ("id", "number", "votes", "created_at")

    def create(self, validated_data):
        validated_data["workshop"] = self.context["workshop"]
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
