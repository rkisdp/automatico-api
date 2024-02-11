from django.db.models import Avg
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
    ordering_fields = ("id", "rating")

    @extend_schema(
        operation_id="list-workshop-reviews",
        summary="List workshop reviews",
        description="Lists all reviews for a workshop",
    )
    def get(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        headers = self._get_rating_headers()
        response = self._add_headers_to_response(response, headers)
        return response

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

    def _add_headers_to_response(self, response, headers):
        for key, value in headers.items():
            response[key] = value
        return response

    def _get_rating_headers(self):
        headers = {
            "X-Rating-Average": self.get_queryset().aggregate(
                rating_average=Avg("rating")
            )["rating_average"],
            "X-5-Star-Rating": self.get_queryset().filter(rating=5).count(),
            "X-4-Star-Rating": self.get_queryset()
            .filter(rating__gte=4, rating__lt=5)
            .count(),
            "X-3-Star-Rating": self.get_queryset()
            .filter(rating__gte=3, rating__lt=4)
            .count(),
            "X-2-Star-Rating": self.get_queryset()
            .filter(rating__gte=2, rating__lt=3)
            .count(),
            "X-1-Star-Rating": self.get_queryset()
            .filter(rating__gte=1, rating__lt=2)
            .count(),
        }
        return headers
