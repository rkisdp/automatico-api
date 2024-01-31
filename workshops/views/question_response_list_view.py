from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from questions.models import QuestionResponseModel

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionResponseListView(
    MultipleFieldLookupMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = QuestionResponseModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "question_id"
    lookup_fields = ("question_id", "id")
    lookup_url_kwargs = ("question_id", "response_id")
    ordering = ("id",)
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")

    @extend_schema(
        operation_id="List question responses",
        description="List question responses",
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="Create question response",
        description="Create question response",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_versioned_module(version, "questions")
        return getattr(module, "QuestionResponseSerializer")