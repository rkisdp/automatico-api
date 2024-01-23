from importlib import import_module

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from workshops.models import WorkshopContactModel


class WorkshopContactDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkshopContactModel.objects.all()
    lookup_field = "id"

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
        return getattr(module, "WorkshopContactListSerializer")
