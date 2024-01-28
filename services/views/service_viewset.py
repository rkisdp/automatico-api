from drf_spectacular.utils import extend_schema
from rest_framework import mixins

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
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
