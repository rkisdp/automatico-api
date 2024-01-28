from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView

SCHEMA_TAGS = ("users",)


@extend_schema(tags=SCHEMA_TAGS)
class UserProfileView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        operation_id="get-the-authenticated-user",
        summary="Get the authenticated user",
        description=(
            "Provides information about the currently authenticated user."
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="update-the-authenticated-user",
        summary="Update the authenticated user",
        description=(
            "Update the information of the currently authenticated user."
        ),
    )
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete-the-authenticated-user",
        summary="Delete the authenticated user",
        description="Delete the account of the currently authenticated user.",
        responses={204: None},
        deprecated=True,
        tags=(*SCHEMA_TAGS, "deprecated"),
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        if not instance.is_active:
            return
        instance.is_active = False
        instance.save()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        try:
            return getattr(module, "PrivateUserSerializer")
        except AttributeError:
            return getattr(module, "UserProfileSerializer")
