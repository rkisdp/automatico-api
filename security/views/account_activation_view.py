from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class AccountActivationView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        module = import_module(
            f"security.serializers.{version.replace('.', '_')}"
        )
        serializer = getattr(module, "AccountActivationSerializer")
        return serializer
