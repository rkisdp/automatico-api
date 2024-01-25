from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from reviews.models import ReviewPhotoModel

SCHEMA_TAGS = ("deprecated",)


@extend_schema(deprecated=True, tags=SCHEMA_TAGS)
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

    @extend_schema(
        description="Use `/reviews/{review_id}/photo/` instead.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Use `/reviews/{review_id}/photo/` instead.",
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
        return getattr(module, "ReviewPhotoSerializer")
