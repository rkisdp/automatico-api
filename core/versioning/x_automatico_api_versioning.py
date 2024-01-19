from django.utils.translation import gettext_lazy as _
from rest_framework.versioning import BaseVersioning


class XAutoMaticoAPIVersioning(BaseVersioning):
    invalid_version_message = _(
        "Invalid version in X-AutoMatico-API-Version header."
    )

    default_version = "0"
    allowed_versions = ("0",)

    def determine_version(self, request, *args, **kwargs):
        return request.META.get("HTTP_X_AUTOMATICO_API_VERSION", None)
