from django.contrib.auth import get_user_model
from rest_framework import serializers

from questions.models import QuestionModel
from workshops.models import WorkshopModel


class QuestionSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = QuestionModel
        fields = (
            "id",
            "client",
            "client_id",
            "workshop",
            "workshop_id",
            "question",
            "questioned_at",
        )
        read_only_fields = ("id", "questioned_at")
