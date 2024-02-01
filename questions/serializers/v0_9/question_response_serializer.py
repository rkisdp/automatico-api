from rest_framework import serializers

from questions.models import QuestionResponseModel
from users.serializers.v0_9 import UserListSerializer


class QuestionResponseSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    # question_url = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     source="question",
    #     view_name="workshops:questions",
    #     lookup_field="id",
    #     lookup_url_kwarg="question_id",
    # )

    class Meta:
        model = QuestionResponseModel
        fields = (
            "id",
            "body",
            "user",
            # "question_url",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["question_id"] = self.context["question_id"]
        return super().create(validated_data)
