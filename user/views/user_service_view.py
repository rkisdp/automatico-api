from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from core import mixins
from core.generics import GenericAPIView
from services.models import ServiceModel

SCHEMA_TAGS = ("services",)


@extend_schema(tags=SCHEMA_TAGS)
class UserServiceView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = ServiceModel.objects.none()
    permission_classes = (IsAuthenticated,)
    ordering = ("id",)
    ordering_fields = ("id", "created_at", "closed_at")
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
    @method_decorator(cache_control(private=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return ServiceModel.objects.filter(vehicle__owner=self.request.user)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "services")
        return getattr(module, "PrivateServiceSerializer")
