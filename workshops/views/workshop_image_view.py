from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.parsers import FormParser, MultiPartParser

from core import mixins
from core.generics import GenericAPIView
from workshops.models import Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopImageView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = Workshop.global_objects.all()
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"

    @extend_schema(
        operation_id="upload-image-for-a-workshop",
        summary="Upload image for a workshop",
        description=(
            "Uploads the image for the workshop. The current image will be "
            "deleted. The authenticated user must be the owner of the workshop."
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete-image-for-a-workshop",
        summary="Delete image for a workshop",
        description=(
            "Delete the image for the workshop. The authenticated user must "
            "be the owner of the workshop."
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.image.delete()
