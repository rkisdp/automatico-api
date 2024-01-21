from importlib import import_module

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

SCHEMA_NAME = "users"


@extend_schema(tags=[SCHEMA_NAME])
class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = get_user_model().objects.all()
    lookup_field = "id"
    ordering = ("id",)
    ordering_fields = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]

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
        module = import_module(f"users.serializers.{version.replace('.', '_')}")
        serializer = getattr(module, "UserSerializer")
        return serializer
