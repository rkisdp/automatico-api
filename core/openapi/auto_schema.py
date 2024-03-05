from drf_spectacular.openapi import AutoSchema as BaseAutoSchema
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from rest_framework.settings import api_settings


class AutoSchema(BaseAutoSchema):
    _global_params = (
        OpenApiParameter(
            name="Accept-Language",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Response language.",
            enum=("en", "es"),
            default="en",
        ),
        OpenApiParameter(
            name="X-AutoMatico-API-Version",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="API version.",
            enum=tuple(api_settings.ALLOWED_VERSIONS),
        ),
        OpenApiParameter(
            name="Location",
            type=OpenApiTypes.URI,
            location=OpenApiParameter.HEADER,
            description="Location of the response.",
            response=[201],
        ),
        OpenApiParameter(
            name="Date",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Date of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Server",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Server name of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Allow",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Allowed methods of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Vary",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Vary of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Content-Language",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Content language of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="X-Frame-Options",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="X-Frame-Options of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Content-Length",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Content-Length of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="X-Content-Type-Options",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="X-Content-Type-Options of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Referrer-Policy",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Referrer-Policy of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="Cross-Origin-Opener-Policy",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.HEADER,
            description="Cross-Origin-Opener-Policy of the request.",
            response=True,
        ),
        OpenApiParameter(
            name="format",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            exclude=True,
        ),
    )

    def get_override_parameters(self):
        self._global_params[1].default = self.view.request.version
        return self._global_params

    def _is_create_operation(self):
        if self.get_operation_id().startswith("add"):
            return False

        if self.view.request.method == "POST":
            return True
        return super()._is_create_operation()

    def _get_paginator(self):
        return None
