from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions

from vehicles.models import VehicleModel
from vehicles.permissions import IsOwnerPermission
from vehicles.serializers import VehicleSerializer


class VehicleView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (DjangoModelPermissions, IsOwnerPermission)
    lookup_field = "id"
    ordering = ("id",)
