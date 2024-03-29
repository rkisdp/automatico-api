from django.contrib.gis.db.models import Q
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView
from workshops.models import Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopListRecommendedView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = Workshop.objects.all()
    filter_backends = ()

    @extend_schema(
        operation_id="list-recommended-workshops",
        summary="List recommended workshops",
        description=(
            "Lists workshops according to your current location and vehicles "
            "brands."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
        parameters=(
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
        brands_filter = self._get_brands_filter()
        distance_filter = self._get_distance_filter()
        return queryset.filter(distance_filter | brands_filter).distinct()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "MinimalWorkshopSerializer")

    def _get_brands_filter(self):
        user = self.request.user
        if user.is_anonymous:
            return Q()
        user_vehicles_brands = user.vehicles.values_list(
            "brand__name",
            flat=True,
        )
        return Q(brands__name__in=user_vehicles_brands)

    def _get_distance_filter(self):
        try:
            lat, lon = self.request.META.get("HTTP_X_USER_LOCATION").split(",")
        except (AttributeError, ValueError):
            lat, lon = None, None
        if lat is None or lon is None:
            return Q()

        user_location = Point(float(lon), float(lat), srid=4326)
        return Q(
            location__isnull=False,
            location__distance_lte=(user_location, 5 * 1000),
        )
