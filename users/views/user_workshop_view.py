from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("users",)


@extend_schema(tags=SCHEMA_TAGS)
class UserWorkshopView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = WorkshopModel.objects.none()
    lookup_field = "id"
    lookup_url_kwarg = "user_id"
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-workshops-for-a-user",
        summary="List workshops for a user",
        description=(
            "Lists workshops for the specified user."
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
                description="The number of results to return per page (max 100).",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
            OpenApiParameter(
                name="user_id",
                description="The user ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_object(self):
        user_id = self.kwargs[self.lookup_url_kwarg]
        return get_user_model().objects.get(id=user_id)

    def get_queryset(self):
        user = self.get_object()
        return user.workshops.all()

    def _get_versioned_serializer_class(self, version):
        module = self._get_module(version, "workshops")
        return getattr(module, "WorkshopListSerializer")
