from importlib import import_module
from rest_framework.generics import ListCreateAPIView

from workshops.models import WorkshopModel


class UserWorkshopView(ListCreateAPIView):
    queryset = WorkshopModel.objects.none()
    ordering = ("id",)

    def get_queryset(self):
        return WorkshopModel.objects.filter(owner=self.request.user)

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
        module = import_module(f"user.serializers.{version.replace('.', '_')}")
        serializer = getattr(module, "UserWorkshopSerializer")
        return serializer
