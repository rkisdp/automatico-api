from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from workshops.models import SpecialityModel, WorkshopModel


class WorkshopSpecialityListView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = SpecialityModel.objects.none()
    lookup_field = "id"
    ordering = ("id",)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return SpecialityModel.objects.filter(workshop_specialities=workshop)

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
        if self.request.method == "PUT":
            return getattr(module, "WorkshopSpecialityDetailSerializer")
        return getattr(module, "WorkshopSpecialityListSerializer")


from importlib import import_module
