from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class PreconditionFailed(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = _(
        "The precondition given in one or more of the request-header fields "
        "evaluated to false when it was tested on the server."
    )
    default_code = "precondition_failed"
