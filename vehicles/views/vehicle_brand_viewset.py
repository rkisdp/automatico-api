from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from vehicles.models import VehicleBrandModel
from vehicles.serializers import VehicleBrandSerializer


class VehicleBrandViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = VehicleBrandModel.objects.all()
    serializer_class = VehicleBrandSerializer
    lookup_field = "id"
    ordering = ("id",)
