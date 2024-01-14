from rest_framework.viewsets import ModelViewSet

from workshops.models import WorkshopContactModel
from workshops.serializers import WorkshopContactSerializer


class WorkshopContactViewSet(ModelViewSet):
    queryset = WorkshopContactModel.objects.all()
    serializer_class = WorkshopContactSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
