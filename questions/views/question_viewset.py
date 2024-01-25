from importlib import import_module

from rest_framework.viewsets import ModelViewSet

from questions.models import QuestionModel


class QuestionViewSet(ModelViewSet):
    queryset = QuestionModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "question_id"
    ordering = ("id",)
    filterset_fields = ("workshop", "question")
    search_fields = ("workshop", "question")
    ordering_fields = ("workshop", "question")

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
        return getattr(module, "QuestionSerializer")
