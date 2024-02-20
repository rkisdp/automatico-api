from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from services.models import ServiceModel

SCHEMA_TAGS = ("services",)


@extend_schema(tags=SCHEMA_TAGS)
class ServiceView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = ServiceModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "service_id"

    @extend_schema(
        operation_id="get-a-service",
        summary="Get a service",
        description="Gets a service.",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "PrivateServiceSerializer")
