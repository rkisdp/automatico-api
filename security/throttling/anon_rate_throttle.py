from rest_framework.throttling import AnonRateThrottle as BaseAnonRateThrottle

from .header_rate_throttle import HeaderRateThrottle


class AnonRateThrottle(
    HeaderRateThrottle,
    BaseAnonRateThrottle,
):
    pass
