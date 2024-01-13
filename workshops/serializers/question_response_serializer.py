from rest_framework import serializers

from workshops.models import QuestionResponseModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponseModel
        fields = ("id", "question", "response")
        read_only_fields = ("id",)
