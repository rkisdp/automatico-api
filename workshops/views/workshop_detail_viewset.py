from rest_framework.generics import RetrieveUpdateDestroyAPIView

from workshops.models import WorkshopModel
from workshops.serializers import WorkshopDetailSerializer


class WorkshopDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkshopModel.objects.all()
    serializer_class = WorkshopDetailSerializer
    lookup_field = "id"
