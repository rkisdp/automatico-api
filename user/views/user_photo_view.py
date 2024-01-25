from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.generics import GenericAPIView

SCHEMA_TAGS = ("user",)


@extend_schema(tags=SCHEMA_TAGS)
class UserPhotoView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        operation_id="upload-image-for-the-authenticated-user",
        summary="Upload image for the authenticated user",
        description=(
            "Uploads the image for the currently authenticated user. The "
            "current image will be deleted."
        ),
        responses={204: None},
    )
    def put(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        operation_id="delete-image-for-the-authenticated-user",
        summary="Delete image for the authenticated user",
        description="Delete the image for the currently authenticated user.",
    )
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
