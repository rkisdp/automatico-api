from rest_framework.generics import RetrieveUpdateDestroyAPIView

from workshops.models import WorkshopContactModel
from workshops.serializers import WorkshopContactListSerializer


class WorkshopContactDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkshopContactModel.objects.all()
    serializer_class = WorkshopContactListSerializer
    lookup_field = "id"
