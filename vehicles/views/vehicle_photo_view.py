from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import DjangoModelPermissions

from vehicles.models import VehicleModel
from vehicles.permissions import IsOwnerPermission
from vehicles.serializers import VehiclePhotoSerializer


class VehiclePhotoView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = VehicleModel.objects.all()
    serializer_class = VehiclePhotoSerializer
    permission_classes = (DjangoModelPermissions, IsOwnerPermission)
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "id"

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
