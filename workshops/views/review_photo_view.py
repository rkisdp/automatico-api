from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.parsers import FormParser, MultiPartParser

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from workshops.models import ReviewModel

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewPhotoView(
    MultipleFieldLookupMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = ReviewModel.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    lookup_fields = ("workshop_id", "id")
    lookup_url_kwargs = ("workshop_id", "review_id")
    ordering = ("id",)
    filterset_fields = ("review",)
    search_fields = ("review",)
    ordering_fields = ("review",)

    @extend_schema()
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema()
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewPhotoSerializer")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["review"] = self.get_object()
        return context
