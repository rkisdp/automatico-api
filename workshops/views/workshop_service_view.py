from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView, get_object_or_404
from services.models import Service
from workshops.models import Workshop

SCHEMA_TAGS = ("services",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopServiceView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = Service.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    filterset_fields = ("vehicle__plate", "vehicle__vin")
    search_fields = ("vehicle__plate", "vehicle__vin")
    ordering_fields = (
        "vehicle__plate",
        "vehicle__vin",
        "number",
        "created_at",
        "closed_at",
    )

    @extend_schema(
        operation_id="list-workshop-services",
        summary="List workshop services",
        description="Lists workshop services",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
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
                description="The number of results to return per page (max 100).",
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
        operation_id="create-service",
        summary="Request a service",
        description="Requests a service",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
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
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Workshop.global_objects.all(), id=workshop_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "services")
        return getattr(module, "PrivateServiceSerializer")
