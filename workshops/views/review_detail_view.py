from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from workshops.models import ReviewModel

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewDetailView(
    MultipleFieldLookupMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = ReviewModel.objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "review_number")

    @extend_schema(
        operation_id="retrieve-a-review",
        summary="Retrieve a review",
        description="Retrieves a review for a workshop",
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="update-a-review",
        summary="Update a review",
        description="Updates a review for a workshop",
    )
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete-a-review",
        summary="Delete a review",
        description="Deletes a review for a workshop",
    )
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewSerializer")