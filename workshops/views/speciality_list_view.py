from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from workshops.models import SpecialityModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class SpecialityListView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = SpecialityModel.objects.all()
    ordering = ("id",)
    search_fields = ("name",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list_specialities",
        description="List all specialities",
        summary="List all specialities",
        parameters=(
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
