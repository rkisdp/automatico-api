from rest_framework.generics import ListCreateAPIView

from user.serializers import UserVehicleSerializer
from vehicles.models import VehicleModel


class UserVehicleView(ListCreateAPIView):
    queryset = VehicleModel.objects.none()
    serializer_class = UserVehicleSerializer
    ordering = ("id",)

    def get_queryset(self):
        return VehicleModel.objects.filter(owner=self.request.user)
