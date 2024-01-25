from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from vehicles.models import VehicleBrandModel

SCHEMA_TAGS = ("vehicles",)


@extend_schema(tags=SCHEMA_TAGS)
class VehicleBrandListView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = VehicleBrandModel.objects.all()
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-vehicle-brands",
        summary="List vehicle brands",
        description="Lists the vehicle brands.",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_module(version)
        return getattr(module, "VehicleBrandSerializer")
