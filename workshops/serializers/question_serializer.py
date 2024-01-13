from rest_framework import serializers

from workshops.models import QuestionModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ("id", "workshop", "question")
        read_only_fields = ("id",)
