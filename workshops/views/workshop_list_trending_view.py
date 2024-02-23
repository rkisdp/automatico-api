from datetime import timedelta

from django.db.models import Avg
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView
from vehicles.models import VehicleBrand
from workshops.models import Speciality, Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopListTrendingView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = Workshop.objects.all()
    filter_backends = ()

    @extend_schema(
        operation_id="list-trending-workshops",
        summary="List trending workshops",
        description=(
            "Lists trending workshops."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
        parameters=(
            OpenApiParameter(
                name="brands",
                description="Filter by vehicle brands.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=VehicleBrand.objects.values_list("name", flat=True),
                many=True,
                explode=False,
            ),
            OpenApiParameter(
                name="specialities",
                description="Filter by specialities.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=Speciality.objects.values_list("name", flat=True),
                many=True,
                explode=False,
            ),
            OpenApiParameter(
                name="page",
                description="The page number of the results to fetch.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=1,
            ),
            OpenApiParameter(
                name="page_size",
                description=(
                    "The number of results to return per page (max 100)."
                ),
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
            OpenApiParameter(
                name="X-User-Location",
                description=(
                    "The user's location in the format `<latitude>,<longitude>`."
                ),
                type=OpenApiTypes.STR,
                location=OpenApiParameter.HEADER,
                pattern=r"^-?\d+(\.\d+)?,-?\d+(\.\d+)?$",
            ),
        ),
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = (
            queryset.filter(
                reviews__created_at__gte=timezone.now() - timedelta(days=30),
            )
            .annotate(recent_rating=Avg("reviews__rating"))
            .order_by("-recent_rating")
        )
        return queryset

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "MinimalWorkshopSerializer")
