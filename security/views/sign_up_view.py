from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView

from ..serializers import SignUpSerializer

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class SignUpView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = SignUpSerializer
