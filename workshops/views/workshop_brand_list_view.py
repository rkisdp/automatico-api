from rest_framework import mixins
from rest_framework.generics import ListAPIView, get_object_or_404
from vehicles.models import VehicleBrandModel
from workshops.models import WorkshopModel
from workshops.serializers import (
    WorkshopBrandDetailSerializer,
    WorkshopBrandListSerializer,
)


class WorkshopBrandListView(
    mixins.UpdateModelMixin,
    ListAPIView,
):
    serializer_class = WorkshopBrandListSerializer
    lookup_field = "id"
    ordering = ("id",)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return VehicleBrandModel.objects.filter(workshop_brands=workshop)

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return WorkshopBrandDetailSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context
