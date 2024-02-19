from drf_spectacular.views import (
    SpectacularRedocView as BaseSpectacularRedocView,
)
from rest_framework.versioning import QueryParameterVersioning

from security.throttling import AnonRateThrottle


class SpectacularRedocView(BaseSpectacularRedocView):
    versioning_class = QueryParameterVersioning
    throttle_classes = (AnonRateThrottle,)
