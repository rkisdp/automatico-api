from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from core.serializers.v0_8 import StringRelatedHyperLinkSerializer
from questions.models import QuestionModel, QuestionResponseModel
from workshops.models import WorkshopModel


class QuestionResponseSerializer(serializers.ModelSerializer):
    client = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="users:users-detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )
    client_id = serializers.PrimaryKeyRelatedField(
        source="client",
        queryset=get_user_model().objects.all(),
        write_only=True,
    )
    workshop = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
    )
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop",
        queryset=WorkshopModel.objects.all(),
        write_only=True,
    )
    question = StringRelatedHyperLinkSerializer(
        read_only=True,
        view_name="questions:detail",
        lookup_field="id",
        lookup_url_kwarg="question_id",
    )
    question_id = serializers.PrimaryKeyRelatedField(
        source="question",
        queryset=QuestionModel.objects.all(),
        write_only=True,
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
            "client",
            "client_id",
            "workshop",
            "workshop_id",
            "question",
            "question_id",
            "response",
            "responded_at",
            "url",
        )
        read_only_fields = ("id", "responded_at")
