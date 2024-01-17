from rest_framework.generics import ListCreateAPIView

from user.serializers import UserWorkshopSerializer
from workshops.models import WorkshopModel


class UserWorkshopView(ListCreateAPIView):
    queryset = WorkshopModel.objects.none()
    serializer_class = UserWorkshopSerializer
    ordering = ("id",)

    def get_queryset(self):
        return WorkshopModel.objects.filter(owner=self.request.user)
