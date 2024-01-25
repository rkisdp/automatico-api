from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from vehicles.models import VehicleModel

SCHEMA_TAGS = ("user",)


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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.vehicles.all()
