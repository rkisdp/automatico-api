from django.utils.translation import gettext_lazy as _
from rest_framework.versioning import BaseVersioning

from core.exceptions import ApiVersionError


class XAutoMaticoAPIVersioning(BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        version = self._get_version(request)
        if not self.is_allowed_version(version):
            raise ApiVersionError(self.invalid_version_message)
        return version

    def _get_version(self, request):
        return request.META.get(
            "HTTP_X_AUTOMATICO_API_VERSION", self.default_version
        )

    @property
    def invalid_version_message(self):
        if len(self.allowed_versions) > 1:
            return _(
                "Invalid version in X-AutoMatico-API-Version header. Allowed "
                f"versions are {', '.join(self.allowed_versions[:-1])} and "
                f"{self.allowed_versions[-1]}."
            )
        return _(
            "Invalid version in X-AutoMatico-API-Version header. Allowed "
            f"version is {self.allowed_versions[0]}."
        )
