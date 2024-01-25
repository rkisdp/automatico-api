from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from vehicles.models import VehicleBrandModel
from workshops.filters import WorkshopFilterSet
from workshops.models import SpecialityModel, WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = WorkshopModel.objects.all()
    ordering = ("id",)
    filterset_class = WorkshopFilterSet
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [SearchFilter]
    search_fields = ("name", "specialities__name", "brands__name")
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-workshops",
        summary="List workshops",
        description=(
            "Lists all workshops in the order that they were created."
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
                enum=VehicleBrandModel.objects.values_list("name", flat=True),
                many=True,
                explode=False,
            ),
            OpenApiParameter(
                name="specialities",
                description="Filter by specialities.",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=SpecialityModel.objects.values_list("name", flat=True),
                many=True,
                explode=False,
            ),
            OpenApiParameter(
                name="ordering",
                description="Which field to use when ordering the results.",
                type=OpenApiTypes.STR,
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
                description="A page number within the paginated result set.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=1,
            ),
            OpenApiParameter(
                name="page_size",
                description="Number of results to return per page.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create-a-workshop-for-the-authenticated-user",
        summary="Create a workshop for the authenticated user",
        description="Creates a new workshop for the authenticated user.",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
