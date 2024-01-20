from importlib import import_module
from rest_framework.generics import ListAPIView

from services.models import ServiceModel


class UserServiceView(ListAPIView):
    queryset = ServiceModel.objects.none()
    ordering = ("id",)

    def get_queryset(self):
        return ServiceModel.objects.filter(vehicle__owner=self.request.user)

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
        serializer = getattr(module, "UserServiceSerializer")
        return serializer
