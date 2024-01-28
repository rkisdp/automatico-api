from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from vehicles.models import VehicleBrandModel

SCHEMA_TAGS = ("vehicles", "deprecated")


@extend_schema(tags=SCHEMA_TAGS)
class VehicleBrandDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = VehicleBrandModel.objects.all()
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
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "VehicleBrandSerializer")
