from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class UserProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses={"204": None})
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

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
        try:
            return getattr(module, "UserProfileSerializer")
        except AttributeError:
            return getattr(module, "ProfileSerializer")
