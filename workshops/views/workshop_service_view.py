from importlib import import_module

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.settings import api_settings

from core.generics import GenericAPIView
from services.models import ServiceModel
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopServiceView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = ServiceModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    filterset_fields = ("vehicle__plate", "vehicle__vin")
    search_fields = ("vehicle__plate", "vehicle__vin")
    ordering_fields = ("vehicle__plate", "vehicle__vin")

    @extend_schema(
        operation_id="list_workshop_services",
        description="List workshop services",
        summary="List workshop services by workshop id",
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
                description="The page number of the results to fetch.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=1,
            ),
            OpenApiParameter(
                name="page_size",
                description="The number of results to return per page (max 100)..",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create_workshop_services",
        description="Request a workshop service",
        summary="Request workshop service by workshop id",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        workshop = self.get_object()
        return self.queryset.filter(workshop=workshop)

    def get_object(self):
        workshop_id = self.kwargs.get("workshop_id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

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
        return getattr(module, "WorkshopServiceListSerializer")
