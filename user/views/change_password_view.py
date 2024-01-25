from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.generics import GenericAPIView

SCHEMA_TAGS = ("user",)


@extend_schema(tags=SCHEMA_TAGS)
class ChangePasswordView(
    mixins.UpdateModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        operation_id="change-authenticated-user-password",
        summary="Change authenticated user password",
        description=(
            "Changes the password of the currently authenticated user. The "
            "current password can not be used as the new password."
        ),
        responses={204: None},
    )
    def put(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        return self.request.user
