from importlib import import_module

from rest_framework import mixins
from rest_framework.generics import ListAPIView, get_object_or_404

from vehicles.models import VehicleModel
from workshops.models import WorkshopModel


class WorkshopVehicleListView(
    mixins.UpdateModelMixin,
    ListAPIView,
):
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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context

    def get_serializer_class(self):
        version = self._get_version()
        serializer = self._get_versioned_serializer_class(version)
        return serializer

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"workshops.serializers.{version.replace('.', '_')}"
        )
        if self.request.method == "PUT":
            serializer = getattr(module, "WorkshopVehicleDetailSerializer")
        serializer = getattr(module, "WorkshopVehicleListSerializer")
        return serializer
