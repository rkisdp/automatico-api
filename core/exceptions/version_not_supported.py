from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class VersionNotSupported(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(
        "The requested version for this resource is not supported."
    )
    default_code = "version_not_supported"
