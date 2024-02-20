from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from services.models import ServiceStatusModel

SCHEMA_TAGS = ("services", "deprecated")


@extend_schema(tags=SCHEMA_TAGS, deprecated=True)
class ServiceStatusDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = ServiceStatusModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "status_id"

    @extend_schema(
        operation_id="get-a-service-status",
        summary="Get a service status",
        description="Gets a service status.",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ServiceStatusSerializer")
