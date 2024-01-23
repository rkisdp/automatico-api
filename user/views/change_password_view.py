from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class ChangePasswordView(mixins.UpdateModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses={204: None})
    def put(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        return self.request.user

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
        return getattr(module, "ChangePasswordSerializer")
