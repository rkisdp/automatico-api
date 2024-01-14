from rest_framework import viewsets

from services.models import ServiceHistoryModel
from services.serializers import ServiceHistorySerializer


class ServiceHistoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceHistoryModel.objects.all()
    serializer_class = ServiceHistorySerializer
    lookup_field = "id"
    ordering = ("id",)
