from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView

from core.generics import GenericAPIView

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class AccessTokenView(GenericAPIView, TokenObtainPairView):
    @extend_schema(
        operation_id="Obtain access token",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
