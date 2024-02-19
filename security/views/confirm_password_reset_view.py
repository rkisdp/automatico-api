from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response

from core.generics import GenericAPIView

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class ConfirmPasswordResetView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
