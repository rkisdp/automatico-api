from importlib import import_module

from rest_framework.viewsets import ModelViewSet
from workshops.models import QuestionResponseModel


class QuestionResponseViewSet(ModelViewSet):
    queryset = QuestionResponseModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")

    def get_serializer_class(self):
        version = self._get_version()
        serializer = self._get_versioned_serializer_class(version)
        return serializer

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
        serializer = getattr(module, "QuestionResponseSerializer")
        return serializer
