from rest_framework.viewsets import ModelViewSet

from workshops.models import WorkshopContactModel
from workshops.serializers import WorkshopContactSerializer


class WorkshopContactViewSet(ModelViewSet):
    queryset = WorkshopContactModel.objects.all()
    serializer_class = WorkshopContactSerializer
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)
    lookup_field = "id"
