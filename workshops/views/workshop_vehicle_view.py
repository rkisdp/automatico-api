from importlib import import_module

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from vehicles.models import VehicleModel
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopVehicleView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView,
):
    queryset = VehicleModel.objects.none()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)

    @extend_schema(
        operation_id="list_workshop_vehicles",
        description="List workshop vehicles",
        summary="List workshop vehicles by workshop id",
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
        operation_id="update_workshop_vehicles",
        description="Update workshop vehicles",
        summary="Update workshop vehicles by workshop id",
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
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return VehicleModel.objects.filter(workshop_vehicles=workshop)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"workshops.serializers.{version.replace('.', '_')}"
        )
        if self.request.method == "PUT":
            return getattr(module, "WorkshopVehicleDetailSerializer")
        return getattr(module, "WorkshopVehicleListSerializer")