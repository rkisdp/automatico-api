from rest_framework.generics import RetrieveUpdateDestroyAPIView

from vehicles.models import VehicleModel
from vehicles.serializers import VehicleSerializer


class VehicleView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = "id"
    ordering = ("id",)
