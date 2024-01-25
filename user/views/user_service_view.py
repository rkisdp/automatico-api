from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from services.models import ServiceModel

SCHEMA_TAGS = ("user",)


@extend_schema(tags=SCHEMA_TAGS)
class UserServiceView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = ServiceModel.objects.none()
    permission_classes = (IsAuthenticated,)
    ordering = ("id",)
    ordering_fields = ("id", "start_date", "end_date")
    filterset_fields = ("histories__status__name",)

    @extend_schema(
        operation_id="list-the-services-for-the-authenticated-user",
        summary="List the services for the authenticated user",
        description=(
            "Lists the services for the currently authenticated user."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return ServiceModel.objects.filter(vehicle__owner=self.request.user)

    def _get_versioned_serializer_class(self, version):
        module = self._get_module(version, "services")
        return getattr(module, "ServiceSerializer")
