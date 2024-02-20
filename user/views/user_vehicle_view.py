from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from core import mixins
from core.generics import GenericAPIView
from vehicles.models import VehicleModel

SCHEMA_TAGS = ("vehicles",)


@extend_schema(tags=SCHEMA_TAGS)
class UserVehicleView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    queryset = VehicleModel.objects.none()
    ordering = ("id",)
    ordering_fields = ("id", "brand", "model")
    search_fields = ("brand__name", "model", "nickname", "plate", "vin")
    filterset_fields = ("brand", "model", "year", "is_archived")

    @extend_schema(
        operation_id="list-the-vehicles-for-the-authenticated-user",
        summary="List the vehicles for the authenticated user",
        description=(
            "Lists the vehicles for the currently authenticated user."
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

    @extend_schema(
        operation_id="create-a-vehicle-for-the-authenticated-user",
        summary="Create a vehicle for the authenticated user",
        description="Creates a vehicle for the currently authenticated user.",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.vehicles.all()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "vehicles")
        return getattr(module, "PrivateVehicleSerializer")
