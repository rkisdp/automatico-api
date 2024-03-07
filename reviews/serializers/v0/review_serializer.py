from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from rest_framework.fields import empty

from core.fields.v0 import HyperLinkSelfField
from reviews.models import Review
from services.models import Service
from services.serializers.v0 import ServiceSerializer
from users.serializers.v0 import UserListSerializer

from .review_response_serializer import ReviewResponseSerializer


@extend_schema_serializer(
    component_name="Review",
    deprecate_fields=("message", "client"),
)
class ReviewSerializer(serializers.ModelSerializer):
    body = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    message = serializers.CharField(
        source="body",
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    service = ServiceSerializer(read_only=True)
    user = UserListSerializer(read_only=True)
    client = UserListSerializer(read_only=True, source="user")
    response = ReviewResponseSerializer(read_only=True)
    image_urls = serializers.SerializerMethodField()
    workshop_url = serializers.HyperlinkedRelatedField(
        view_name="workshops:detail",
        lookup_field="id",
        lookup_url_kwarg="workshop_id",
        source="workshop",
        read_only=True,
    )
    url = HyperLinkSelfField(
        view_name="workshops:review-detail",
        lookup_fields=("workshop_id", "number"),
        lookup_url_kwargs=("workshop_id", "review_number"),
    )

    class Meta:
        model = Review
        fields = (
            "id",
            "number",
            "body",
            "message",
            "rating",
            "response",
            "service",
            "user",
            "client",
            "created_at",
            "image_urls",
            "workshop_url",
            "url",
        )
        read_only_fields = ("id", "number", "created_at")

    def get_fields(self):
        fields = super().get_fields()
        if self.context and self.context["request"].method != "GET":
            fields["service"] = serializers.IntegerField(
                write_only=True,
                required=False,
                allow_null=True,
            )
        return fields

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["service"] = ServiceSerializer()
        return validated_data

    def get_image_urls(
        self, obj
    ) -> serializers.ListField(child=serializers.URLField()):
        request = self.context.get("request", None)
        images = []
        for image in obj.images.all():
            if image.image is not None:
                images.append(request.build_absolute_uri(image.image.url))
        return images

    def validate_service(self, value):
        if value is None:
            return None
        try:
            workshop = self.context["workshop"]
            return Service.objects.get(number=value, workshop=workshop)
        except Service.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Service #{value} does not exist.")
            )

    def validate(self, attrs):
        if self.context["request"].method != "POST":
            return attrs

        service = attrs.get("service", None)
        if service is None:
            return attrs

        if service.workshop != self.context["workshop"]:
            raise serializers.ValidationError(
                {"service": _("Service does not belong to this workshop.")}
            )

        if service.vehicle.owner != self.context["request"].user:
            raise serializers.ValidationError(
                {
                    "service": _(
                        "You can only review services for your vehicles."
                    )
                }
            )

        if Review.objects.filter(service=service).exists():
            raise serializers.ValidationError(
                {"service": _("You have already reviewed this service.")}
            )

        # Deprecated 'message' field
        if not any([attrs.get("body", None), attrs.get("message", None)]):
            raise serializers.ValidationError(
                {"service": _("You must provide a body or message.")}
            )

        attrs["body"] = attrs.get("body", attrs.get("message", None))
        return attrs

    def create(self, validated_data):
        validated_data["workshop"] = self.context["workshop"]
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
