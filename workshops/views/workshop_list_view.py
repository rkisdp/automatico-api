from importlib import import_module

from rest_framework.generics import ListCreateAPIView

from workshops.models import WorkshopModel


class WorkshopListView(ListCreateAPIView):
    queryset = WorkshopModel.objects.all()
    ordering = ("id",)
    filterset_fields = ("specialities__name", "brands__name")
    search_fields = (
        "name",
        "specialities__name",
        "brands__name",
    )
    ordering_fields = ("name",)

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
        serializer = getattr(module, "WorkshopListSerializer")
        return serializer
