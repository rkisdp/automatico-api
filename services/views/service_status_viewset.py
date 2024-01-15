from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceStatusModel
from services.serializers import ServiceStatusSerializer


class ServiceStatusViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = ServiceStatusModel.objects.all()
    serializer_class = ServiceStatusSerializer
    lookup_field = "id"
    ordering = ("id",)
