from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from core.mixins import MultipleFieldLookupMixin
from questions.models import QuestionResponseModel

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionResponseViewSet(MultipleFieldLookupMixin, ModelViewSet):
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
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"questions.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "QuestionResponseSerializer")
