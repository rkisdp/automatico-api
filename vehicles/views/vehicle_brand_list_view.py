from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
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
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "VehicleBrandSerializer")
