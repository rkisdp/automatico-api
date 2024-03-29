from django.db.models import Avg
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from core import mixins
from core.generics import GenericAPIView, get_object_or_404
from workshops.models import Workshop

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
        parameters=(
            OpenApiParameter(
                name="ordering",
                description="Which field to use when ordering the results.",
                type=OpenApiTypes.STR,
                many=True,
                explode=False,
                enum=(
                    "-id",
                    "-rating",
                    "id",
                    "rating",
                ),
                default="id",
            ),
        ),
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create-a-review",
        summary="Create a review",
        description="Create a review for a workshop",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if response.status_code != 200:
            return response

        headers = self._get_rating_headers()
        response = self._add_headers_to_response(response, headers)
        return response

    def get_object(self):
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Workshop.global_objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return workshop.reviews.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "reviews")
        return getattr(module, "ReviewSerializer")

    def _add_headers_to_response(self, response, headers):
        for key, value in headers.items():
            response[key] = value
        return response

    def _get_rating_headers(self):
        headers = {
            "X-Rating-Average": round(
                self.get_queryset().aggregate(rating_avg=Avg("rating"))[
                    "rating_avg"
                ]
                or 0,
                1,
            ),
            "X-Rating-5-Star": self.get_queryset().filter(rating=5).count(),
            "X-Rating-4-Star": self.get_queryset()
            .filter(rating__gte=4, rating__lt=5)
            .count(),
            "X-Rating-3-Star": self.get_queryset()
            .filter(rating__gte=3, rating__lt=4)
            .count(),
            "X-Rating-2-Star": self.get_queryset()
            .filter(rating__gte=2, rating__lt=3)
            .count(),
            "X-Rating-1-Star": self.get_queryset()
            .filter(rating__gte=1, rating__lt=2)
            .count(),
        }
        return headers
