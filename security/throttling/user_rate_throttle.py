from rest_framework.throttling import UserRateThrottle as BaseUserRateThrottle

from .header_rate_throttle import HeaderRateThrottle


class UserRateThrottle(
    HeaderRateThrottle,
    BaseUserRateThrottle,
):
    def get_cache_key(self, request, view):
        """
        Same as parent class, but if user is not authenticated, return None.
        """
        if request.user and request.user.is_authenticated:
            ident = request.user.pk
        else:
            return None

        return self.cache_format % {
            "scope": self.scope,
            "ident": ident,
        }
