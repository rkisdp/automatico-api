from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from workshops.models import WorkshopContactModel, WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopContactListView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView,
):
    queryset = WorkshopContactModel.objects.none()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-a-workshop-contacts",
        description="List a workshop contacts",
        summary="List workshop contacts",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
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
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="replace-all-workshop-contacts",
        summary="Replace all workshop contacts",
        description="Replaces all workshop contacts.",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
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
                        ordering, (f"-{field}" for field in ordering)
                    )
                    for field in pair
                ),
                default="id",
                exclude=True,
            ),
            OpenApiParameter(
                name="page",
                description="A page number within the paginated result set.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=1,
                exclude=True,
            ),
            OpenApiParameter(
                name="page_size",
                description="Number of results to return per page.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
                exclude=True,
            ),
        ),
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs.get("workshop_id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return WorkshopContactModel.objects.filter(workshop=workshop)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("workshop_id")
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_module(version)
        if self.request.method == "PUT":
            return getattr(module, "WorkshopContactDetailSerializer")
        return getattr(module, self._get_serializer_name())
