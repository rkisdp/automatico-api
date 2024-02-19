from rest_framework.throttling import SimpleRateThrottle


class HeaderRateThrottle(SimpleRateThrottle):
    """
    Define a custom rate throttle to add rate limit headers.
    """

    def allow_request(self, request, view):
        """
        Same as parent class, but if key is None, return None.
        """
        if self.rate is None:
            return True

        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return None

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()

        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()

    def get_headers(self):
        """
        Construct rate limit headers.
        """
        return {
            "X-RateLimit-Limit": self.num_requests,
            "X-RateLimit-Remaining": self.num_requests - len(self.history),
            "X-RateLimit-Reset": round(self.history[-1]),
            "X-RateLimit-Used": len(self.history),
        }
