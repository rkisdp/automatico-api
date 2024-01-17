from rest_framework.generics import ListAPIView

from services.models import ServiceModel
from user.serializers import UserServiceSerializer


class UserServiceView(ListAPIView):
    queryset = ServiceModel.objects.none()
    serializer_class = UserServiceSerializer
    ordering = ("id",)

    def get_queryset(self):
        return ServiceModel.objects.filter(vehicle__owner=self.request.user)
