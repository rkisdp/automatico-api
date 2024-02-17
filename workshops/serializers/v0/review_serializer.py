from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from rest_framework.fields import empty

from core.fields.v0 import HyperLinkSelfField
from services.models import ServiceModel
from services.serializers.v0 import ServiceSerializer
from users.serializers.v0 import UserListSerializer
from workshops.models import ReviewModel

from .review_response_serializer import ReviewResponseSerializer


@extend_schema_serializer(component_name="Review", deprecate_fields=("score",))
class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        max_digits=2,
        decimal_places=1,
        help_text=_("The rating of the review."),
        required=False,
        allow_null=True,
    )
    score = serializers.DecimalField(
        source="rating",
        max_digits=2,
        decimal_places=1,
        help_text=_("The score of the review."),
        required=False,
        allow_null=True,
    )
    service = ServiceSerializer(read_only=True)
    client = UserListSerializer(read_only=True)
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
        model = ReviewModel
        fields = (
            "id",
            "number",
            "message",
            "rating",
            "score",
            "response",
            "service",
            "client",
            "created_at",
            "image_urls",
            "workshop_url",
            "url",
        )
        read_only_fields = ("id", "number", "created_at")

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        if self.context and self.context["request"].method != "GET":
            self.fields["service"] = serializers.IntegerField(
                write_only=True,
                required=False,
                allow_null=True,
            )

    def get_image_urls(
        self, obj
    ) -> serializers.ListField(child=serializers.URLField()):
        request = self.context.get("request", None)
        images = []
        for image in obj.images.all():
            if image.image is not None:
                images.append(request.build_absolute_uri(image.image.url))
        return images

    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)
        self.fields["service"] = ServiceSerializer()
        return validated_data

    def validate_service(self, value):
        try:
            workshop = self.context["workshop"]
            if value is None:
                return None
            return ServiceModel.objects.get(number=value, workshop=workshop)
        except ServiceModel.DoesNotExist:
            raise serializers.ValidationError(
                _(f"Service #{value} does not exist.")
            )

    def validate(self, attrs):
        if self.context["request"].method == "POST":
            if ReviewModel.objects.filter(
                service=attrs["service"], client=attrs["client"]
            ).exists():
                raise serializers.ValidationError(
                    _("You have already reviewed this service.")
                )

        if attrs.get("rating") is None and attrs.get("score") is None:
            raise serializers.ValidationError(
                _("Rating or score must be provided.")
            )

        attrs["rating"] = attrs.get("rating", attrs.get("score"))
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["workshop"] = self.context["workshop"]
        validated_data["client"] = self.context["request"].user
        return super().create(validated_data)
