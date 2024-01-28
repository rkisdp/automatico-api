from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from questions.models import QuestionResponseModel

SCHEMA_TAGS = ("questions", "deprecated")


@extend_schema(deprecated=True, tags=SCHEMA_TAGS)
class QuestionResponseViewSet(ModelViewSet):
    queryset = QuestionResponseModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")

    @extend_schema(
        description="Use `/questions/{question_id}/reponses` instead.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Use `/questions/{question_id}/reponses` instead.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Use `/questions/{question_id}/reponses/{response_id}` instead.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="This endpoint is deprecated and will be removed",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Use `/questions/{question_id}/reponses/{response_id}` instead.",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="This endpoint is deprecated and will be removed",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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
            f"workshops.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "QuestionResponseSerializer")
