from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView, get_object_or_404
from vehicles.models import Vehicle
from workshops.models import Workshop

SCHEMA_TAGS = ("vehicles",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopVehicleView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView,
):
    queryset = Vehicle.objects.none()
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
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Workshop.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return Vehicle.objects.filter(workshop_vehicles=workshop)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "vehicles")
        if self.request.method == "PUT":
            return getattr(module, "VehicleSerializer")
        return getattr(module, "VehicleSerializer")
