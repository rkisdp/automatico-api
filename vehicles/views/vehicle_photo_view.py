from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from vehicles.models import VehicleModel
from vehicles.permissions import IsOwnerPermission

SCHEMA_TAGS = ("vehicles",)


@extend_schema(tags=SCHEMA_TAGS)
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

    @extend_schema(
        operation_id="upload-image-for-a-vehicle",
        summary="Upload image for a vehicle",
        description=(
            "Uploads the image for the vehicle. The current image will be "
            "deleted. The authenticated user must be the owner of the vehicle."
        ),
        parameters=(
            OpenApiParameter(
                name="vehicle_id",
                description="The vehicle ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
        responses={204: None},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete-image-for-a-vehicle",
        summary="Delete image for a vehicle",
        description=(
            "Delete the image for the vehicle. The authenticated user must "
            "be the owner of the vehicle."
        ),
        parameters=(
            OpenApiParameter(
                name="vehicle_id",
                description="The vehicle ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        if not instance.image:
            return
        instance.image.delete()
