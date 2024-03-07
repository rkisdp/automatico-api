from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from core import mixins
from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from reviews.models import Review

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewResponseView(
    MultipleFieldLookupMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = Review.global_objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "review_number")
    ordering = ("id",)

    @extend_schema()
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if not hasattr(instance, "response"):
            raise NotFound()
        serializer = self.get_serializer(instance.response)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema()
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "reviews")
        return getattr(module, "ReviewResponseSerializer")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["review"] = self.get_object()
        return context
