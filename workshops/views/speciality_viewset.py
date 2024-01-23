from importlib import import_module

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from workshops.models import SpecialityModel


class SpecialityViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = SpecialityModel.objects.all()
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)

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
        return getattr(module, "SpecialitySerializer")
