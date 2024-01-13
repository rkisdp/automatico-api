from rest_framework import viewsets

from services.models import ServiceModel
from services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "id"
