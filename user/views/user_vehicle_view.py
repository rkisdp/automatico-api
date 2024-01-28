from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

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
        return getattr(module, "VehicleSerializer")
