from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from workshops.models import ReviewResponseModel

SCHEMA_TAGS = ("deprecated",)


@extend_schema(deprecated=True, tags=SCHEMA_TAGS)
class ReviewResponseViewSet(ModelViewSet):
    queryset = ReviewResponseModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("review", "response")
    search_fields = ("review", "response")
    ordering_fields = ("review", "response")

    @extend_schema(
        description="Use `/reviews/{review_id}/reponses/` instead.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Use `/reviews/{review_id}/reponses/` instead.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Use `/reviews/{review_id}/reponses/{response_id}` instead.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="This endpoint is deprecated and will be removed",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Use `/reviews/{review_id}/reponses/{response_id}` instead.",
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
        return getattr(module, "ReviewResponseSerializer")
