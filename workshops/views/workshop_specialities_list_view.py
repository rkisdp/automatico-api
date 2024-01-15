from rest_framework.generics import ListCreateAPIView

from workshops.models import WorkshopContactModel
from workshops.serializers import WorkshopContactListSerializer


class WorkshopContactListView(ListCreateAPIView):
    queryset = WorkshopContactModel.objects.all()
    serializer_class = WorkshopContactListSerializer
    lookup_field = "id"
