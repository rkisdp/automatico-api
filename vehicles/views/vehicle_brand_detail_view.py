from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from core import mixins
from core.generics import GenericAPIView
from vehicles.models import VehicleBrand

SCHEMA_TAGS = ("vehicles", "deprecated")


@extend_schema(tags=SCHEMA_TAGS)
class VehicleBrandDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = VehicleBrand.global_objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "brand_id"

    @extend_schema(
        operation_id="get-a-vehicle-brand",
        summary="Get a vehicle brand",
        description="Gets the vehicle brand.",
        deprecated=True,
        parameters=(
            OpenApiParameter(
                name="brand_id",
                description="The brand ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "VehicleBrandSerializer")
