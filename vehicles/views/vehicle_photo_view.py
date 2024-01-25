from importlib import import_module

from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from vehicles.models import VehicleModel
from vehicles.permissions import IsOwnerPermission


class VehiclePhotoView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = VehicleModel.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerPermission)
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "id"
    lookup_url_kwarg = "vehicle_id"
    ordering = ("id",)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self):
        instance = super().get_object()
        if not instance.photo and self.request.method == "DELETE":
            raise ValidationError(
                {"detail": _("Vehicle does not have a photo.")}
            )

        return instance

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
        module = import_module(
            f"vehicles.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "VehiclePhotoSerializer")
