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

    def _get_serializer_module(self, version, module_name=None):
        if module_name is None:
            module_name = self.__module__
            return import_module(
                f"{'.'.join(module_name.split('.')[:-2])}.serializers."
                + version.replace(".", "_")
            )
        return import_module(
            f"{module_name}.serializers.{version.replace('.', '_')}"
        )

    def _get_serializer_name(self):
        return self.__class__.__name__.replace("View", "Serializer")

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        serializer_name = self._get_serializer_name()
        return getattr(module, serializer_name)
