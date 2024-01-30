from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.fields import empty

from core.fields.v0_9 import HyperLinkSelfField
from services.models import ServiceModel
from services.serializers.v0_9 import ServiceSerializer
from users.serializers.v0_9 import UserListSerializer
from workshops.models import ReviewModel


class ReviewSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    client = UserListSerializer(read_only=True)
    workshop_url = serializers.HyperlinkedRelatedField(
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        source="workshop",
        read_only=True,
    )
    url = HyperLinkSelfField(
        view_name="workshops:reviews",
        lookup_field="workshop_id",
    )

    class Meta:
        model = ReviewModel
        fields = (
            "id",
            "service",
            "client",
            "review",
            "score",
            "created_at",
            "workshop_url",
            "url",
        )
        read_only_fields = ("id", "created_at")

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["service"] = serializers.IntegerField(write_only=True)

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["service"] = ServiceSerializer()
        return validated_data

    def validate_service(self, value):
        try:
            workshop_id = self.context["workshop_id"]
            return ServiceModel.objects.get(
                number__iexact=value,
                workshop_id=workshop_id,
            )
        except ServiceModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Service #{value} does not exist.")
            )

    def create(self, validated_data):
        validated_data["workshop_id"] = self.context["workshop_id"]
        # validated_data["service_id"] = self.context["service_id"]
        validated_data["client"] = self.context["request"].user
        return super().create(validated_data)
