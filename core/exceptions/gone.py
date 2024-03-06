from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class Gone(APIException):
    status_code = status.HTTP_410_GONE
    default_detail = _("This resource is no longer available.")
    default_code = "gone"
