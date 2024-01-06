from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from security.serializers import AccountActivationSerializer

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class AccountActivationView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = AccountActivationSerializer

    @extend_schema(
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
