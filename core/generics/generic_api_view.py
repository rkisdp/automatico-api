from importlib import import_module

from rest_framework.generics import GenericAPIView as BaseGenericAPIView


class GenericAPIView(BaseGenericAPIView):
    def get_serializer_class(self):
        return self._get_versioned_serializer_class(self._get_version())

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_module(self, version):
        return import_module(
            f"{'.'.join(self.__module__.split('.')[:-2])}.serializers."
            + version.replace(".", "_")
        )

    def _get_serializer_name(self):
        return self.__class__.__name__.replace("View", "Serializer")

    def _get_versioned_serializer_class(self, version):
        module = self._get_module(version)
        serializer_name = self._get_serializer_name()
        return getattr(module, serializer_name)
