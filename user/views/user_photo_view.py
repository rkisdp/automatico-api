from importlib import import_module

from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class UserPhotoView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        instance = self.get_object()
        self.perform_destroy(instance)
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        instance.photo.delete()

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
        return getattr(module, "UserPhotoSerializer")
