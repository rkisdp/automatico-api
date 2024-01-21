from importlib import import_module

from rest_framework.viewsets import ModelViewSet
from workshops.models import ReviewResponseModel


class ReviewResponseViewSet(ModelViewSet):
    queryset = ReviewResponseModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("review", "response")
    search_fields = ("review", "response")
    ordering_fields = ("review", "response")

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
        serializer = getattr(module, "ReviewResponseSerializer")
        return serializer
