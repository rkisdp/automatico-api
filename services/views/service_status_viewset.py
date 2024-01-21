from importlib import import_module

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceStatusModel


class ServiceStatusViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = ServiceStatusModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)

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
            f"services.serializers.{version.replace('.', '_')}"
        )
        serializer = getattr(module, "ServiceStatusSerializer")
        return serializer
