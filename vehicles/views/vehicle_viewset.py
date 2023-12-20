from rest_framework import viewsets

from vehicles.models import VehicleBrandModel, VehicleModel
from vehicles.serializers import (
    VehicleBrandModelSerializer,
    VehicleModelSerializer,
)


class VehicleBrandModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleBrandModel.objects.all()
    serializer_class = VehicleBrandModelSerializer


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
