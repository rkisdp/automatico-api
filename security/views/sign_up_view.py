from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class SignUpView(CreateAPIView):
    authentication_classes = []
    permission_classes = []

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
            f"security.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "SignUpSerializer")
