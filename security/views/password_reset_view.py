from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PasswordResetSerializer

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class PasswordResetView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PasswordResetSerializer

    @extend_schema(
        operation_id="Request password reset email",
        description="Request password reset email.",
        responses={
            204: None,
        },
    )
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
