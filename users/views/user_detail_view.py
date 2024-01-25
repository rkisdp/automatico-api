from importlib import import_module

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView

SCHEMA_NAME = "users"


@extend_schema(tags=[SCHEMA_NAME])
class UserDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = get_user_model().objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "user_id"

    # def get_serializer_class(self):
    #     version = self._get_version()
    #     return self._get_versioned_serializer_class(version)

    # def _get_version(self):
    #     try:
    #         version = self.request.version
    #     except Exception:
    #         version, _ = self.determine_version(self.request)
    #     return version

    # def _get_versioned_serializer_class(self, version):
    #     module = import_module(f"users.serializers.{version.replace('.', '_')}")
    #     return getattr(module, "UserSerializer")
