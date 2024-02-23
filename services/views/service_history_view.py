from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView, get_object_or_404
from services.models import Service, ServiceHistory

SCHEMA_TAGS = ("services",)


@extend_schema(tags=SCHEMA_TAGS)
class ServiceHistoryView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = ServiceHistory.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "service_id"
    ordering = ("id",)
    ordering_fields = ("id", "status")
    filterset_fields = ("service", "status")

    @extend_schema(
        operation_id="list-service-history",
        summary="List service history",
        description=(
            "Lists the history of a service."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
        parameters=(
            OpenApiParameter(
                name="ordering",
                description="Which field to use when ordering the results.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                many=True,
                explode=False,
                enum=(
                    field
                    for pair in zip(
                        ordering_fields,
                        (f"-{field}" for field in ordering_fields),
                    )
                    for field in pair
                ),
                default="id",
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
                    "The The number of results to return per page (max 100)."
                ),
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
        ),
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create-service-history",
        summary="Create service history",
        description="Creates a new service history.",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        service_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Service.objects.all(), id=service_id)

    def get_queryset(self):
        service = self.get_object()
        return service.histories.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["service"] = self.get_object()
        return context
