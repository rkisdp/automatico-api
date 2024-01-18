from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceModel
from workshops.models import WorkshopModel
from workshops.serializers import WorkshopServiceListSerializer


class WorkshopServiceViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet
):
    queryset = ServiceModel.objects.all()
    serializer_class = WorkshopServiceListSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("vehicle__plate", "vehicle__vin")
    search_fields = ("vehicle__plate", "vehicle__vin")
    ordering_fields = ("vehicle__plate", "vehicle__vin")

    def get_queryset(self):
        workshop = self.get_object()
        return self.queryset.filter(workshop=workshop)

    def get_object(self):
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context
