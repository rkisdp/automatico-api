from rest_framework.generics import ListAPIView

from vehicles.models import VehicleBrandModel
from vehicles.serializers import VehicleBrandSerializer


class VehicleBrandView(ListAPIView):
    queryset = VehicleBrandModel.objects.all()
    serializer_class = VehicleBrandSerializer
