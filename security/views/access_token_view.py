from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt import views

SCHEMA_NAME = "auth"


@extend_schema(tags=[SCHEMA_NAME])
class AccessTokenView(views.TokenObtainPairView):
    @extend_schema(
        operation_id="Obtain access token",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
