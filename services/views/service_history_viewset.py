from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceHistoryModel, ServiceModel
from services.serializers import ServiceHistorySerializer


class ServiceHistoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = ServiceHistoryModel.objects.all()
    serializer_class = ServiceHistorySerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("service", "status")

    def get_object(self):
        service_id = self.kwargs.get("id")
        return get_object_or_404(ServiceModel.objects.all(), id=service_id)

    def get_queryset(self):
        service = self.get_object()
        return ServiceHistoryModel.objects.filter(service=service)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["service_id"] = self.kwargs.get("id")
        return context
