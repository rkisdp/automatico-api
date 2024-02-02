from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from core.generics import GenericAPIView
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    ordering_fields = ("id", "created_at", "score")
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)

    @extend_schema(
        operation_id="list-workshop-reviews",
        summary="List workshop reviews",
        description="Lists all reviews for a workshop",
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create-a-review",
        summary="Create a review",
        description="Create a review for a workshop",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return workshop.reviews.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewSerializer")
