from drf_spectacular.views import (
    SpectacularSwaggerView as BaseSpectacularSwaggerView,
)
from rest_framework.versioning import QueryParameterVersioning

from security.throttling import AnonRateThrottle


class SpectacularSwaggerView(BaseSpectacularSwaggerView):
    versioning_class = QueryParameterVersioning
    throttle_classes = (AnonRateThrottle,)
