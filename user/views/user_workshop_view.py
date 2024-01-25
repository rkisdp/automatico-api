from importlib import import_module

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from workshops.models import WorkshopModel


class UserWorkshopView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = WorkshopModel.objects.none()
    ordering = ("id",)

    def get_queryset(self):
        return WorkshopModel.objects.filter(owner=self.request.user)

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
        module = import_module(f"user.serializers.{version.replace('.', '_')}")
        return getattr(module, "UserWorkshopSerializer")
