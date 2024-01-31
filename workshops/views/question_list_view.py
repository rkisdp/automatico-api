from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from questions.models import QuestionModel

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = QuestionModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "question_id"
    ordering = ("id",)
    filterset_fields = ("workshop", "question")
    search_fields = ("workshop", "question")
    ordering_fields = ("workshop", "question")

    @extend_schema(
        operation_id="List questions",
        description="List questions",
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="Create question",
        description="Create question",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_versioned_module(version, "questions")
        return getattr(module, "QuestionSerializer")
