from importlib import import_module

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

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"security.serializers.v{version.replace('.', '_')}"
        )
        return getattr(module, "AccessTokenSerializer")
