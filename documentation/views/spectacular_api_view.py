from drf_spectacular.views import SpectacularAPIView as BaseSpectacularAPIView
from rest_framework.versioning import QueryParameterVersioning

from security.throttling import AnonRateThrottle


class SpectacularAPIView(BaseSpectacularAPIView):
    versioning_class = QueryParameterVersioning
    throttle_classes = (AnonRateThrottle,)
