from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class SignUpView(
    mixins.CreateModelMixin,
    GenericAPIView,
):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
