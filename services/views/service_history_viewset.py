from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceHistoryModel
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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["service_id"] = self.kwargs.get("id")
        return context
