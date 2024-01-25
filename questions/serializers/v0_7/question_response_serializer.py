from django.contrib.auth import get_user_model
from rest_framework import serializers

from questions.models import QuestionModel, QuestionResponseModel
from workshops.models import WorkshopModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        source="client",
        queryset=get_user_model().objects.all(),
        write_only=True,
    )
    workshop = serializers.StringRelatedField(read_only=True)
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop",
        queryset=WorkshopModel.objects.all(),
        write_only=True,
    )
    question = serializers.StringRelatedField(read_only=True)
    question_id = serializers.PrimaryKeyRelatedField(
        source="question",
        queryset=QuestionModel.objects.all(),
        write_only=True,
    )

    class Meta:
        model = QuestionResponseModel
        fields = (
            "id",
            "client",
            "client_id",
            "workshop",
            "workshop_id",
            "question",
            "question_id",
            "response",
            "responded_at",
        )
        read_only_fields = ("id", "responded_at")
