from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from workshops.models import ReviewModel

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewResponseView(
    MultipleFieldLookupMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = ReviewModel.objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "review_number")
    ordering = ("id",)

    @extend_schema()
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema()
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        review = self.get_object()
        return review.responses.all()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewResponseSerializer")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["review"] = self.get_object()
        return context
