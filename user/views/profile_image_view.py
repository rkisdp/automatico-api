from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from user.serializers import ProfileImageSerializer

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class ProfileImageView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProfileImageSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer.save()

    def perform_destroy(self, instance):
        instance.photo.delete()
