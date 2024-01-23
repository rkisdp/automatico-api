from importlib import import_module

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from workshops.models import ReviewPhotoModel


class ReviewPhotoViewSet(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = ReviewPhotoModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("review",)
    search_fields = ("review",)
    ordering_fields = ("review",)

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
        return getattr(module, "ReviewPhotoSerializer")
