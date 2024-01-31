from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from questions.models import QuestionModel
from users.serializers.v0_9 import UserListSerializer


class QuestionSerializer(serializers.ModelSerializer):
    client = UserListSerializer(read_only=True)
    workshop_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        source="workshop",
    )
    url = HyperLinkSelfField(
        view_name="questions:detail",
        lookup_field="id",
        lookup_url_kwarg="question_id",
    )

    class Meta:
        model = QuestionModel
        fields = (
            "id",
            "number",
            "body",
            "client",
            "created_at",
            "workshop_url",
            "url",
        )
        read_only_fields = ("id", "number", "created_at")
