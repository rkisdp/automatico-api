from rest_framework import serializers

from questions.models import QuestionModel


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ("id", "client", "workshop", "question", "questioned_at")
        read_only_fields = ("id", "questioned_at")
