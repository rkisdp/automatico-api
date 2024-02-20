from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from services.models import ServiceStatusModel

SCHEMA_TAGS = ("services",)


@extend_schema(tags=SCHEMA_TAGS)
class ServiceStatusListView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = ServiceStatusModel.objects.all()
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-service-statuses",
        summary="List service statuses",
        description="Lists the service statuses.",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ServiceStatusSerializer")
