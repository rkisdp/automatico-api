from importlib import import_module

from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceModel
from workshops.models import WorkshopModel


class WorkshopServiceViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = ServiceModel.objects.all()
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

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

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
        return getattr(module, "WorkshopServiceListSerializer")
