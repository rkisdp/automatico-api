from rest_framework.generics import ListAPIView

from services.models import ServiceModel
from user.serializers import UserWorkshopServiceSerializer


class UserWorkshopServiceView(ListAPIView):
    queryset = ServiceModel.objects.none()
    serializer_class = UserWorkshopServiceSerializer
    ordering = ("id",)

    def get_queryset(self):
        return ServiceModel.objects.filter(workshop__owner=self.request.user)
