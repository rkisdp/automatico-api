from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from user.serializers import UserVehicleSerializer
from vehicles.models import VehicleModel


class UserVehicleView(ListCreateAPIView):
    queryset = VehicleModel.objects.none()
    serializer_class = UserVehicleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return VehicleModel.objects.filter(owner=self.request.user)
