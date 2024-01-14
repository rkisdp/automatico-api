from rest_framework import viewsets

from services.models import ServiceStatusModel
from services.serializers import ServiceStatusSerializer


class ServiceStatusViewSet(viewsets.ModelViewSet):
    queryset = ServiceStatusModel.objects.all()
    serializer_class = ServiceStatusSerializer
    lookup_field = "id"
    ordering = ("id",)
