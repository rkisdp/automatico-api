from rest_framework import mixins
from rest_framework.generics import ListAPIView, get_object_or_404

from vehicles.models import VehicleModel
from workshops.models import WorkshopModel
from workshops.serializers import (
    WorkshopVehicleDetailSerializer,
    WorkshopVehicleListSerializer,
)


class WorkshopVehicleListView(
    mixins.UpdateModelMixin,
    ListAPIView,
):
    serializer_class = WorkshopVehicleListSerializer
    lookup_field = "id"
    ordering = ("id",)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return VehicleModel.objects.filter(workshop_vehicles=workshop)

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return WorkshopVehicleDetailSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context
