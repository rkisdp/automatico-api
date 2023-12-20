from rest_framework import viewsets
from services.models import (
    ServiceHistoryModel,
    ServiceModel,
    ServiceStatusModel,
)
from services.serializers import (
    ServiceHistorySerializer,
    ServiceSerializer,
    ServiceStatusSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer


class ServiceHistoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceHistoryModel.objects.all()
    serializer_class = ServiceHistorySerializer


class ServiceStatusViewSet(viewsets.ModelViewSet):
    queryset = ServiceStatusModel.objects.all()
    serializer_class = ServiceStatusSerializer
