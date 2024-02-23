from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from workshops.models import Review

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewDetailView(
    mixins.MultipleFieldLookupMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = Review.objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "review_number")

    @extend_schema(
        operation_id="retrieve-a-review",
        summary="Retrieve a review",
        description="Retrieves a review for a workshop",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
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
        context["workshop"] = self.get_object().workshop
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewSerializer")
