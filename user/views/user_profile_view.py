from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class UserProfileView(RetrieveUpdateAPIView):
    def get_object(self):
        return self.request.user

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
        try:
            serializer = getattr(module, "UserProfileSerializer")
        except AttributeError:
            serializer = getattr(module, "ProfileSerializer")
        return serializer
