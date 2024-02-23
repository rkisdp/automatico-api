from importlib import import_module

from rest_framework.generics import GenericAPIView as BaseGenericAPIView


class GenericAPIView(BaseGenericAPIView):
    def get_serializer_class(self):
        return self._get_versioned_serializer_class(self._get_version())

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_serializer_module(self, version, module_name=None):
        if module_name is None:
            module_name = self.__module__.split(".")[-3]
        return import_module(
            f"{module_name}.serializers.v{version.replace('.', '_')}"
        )

    def _get_serializer_name(self):
        return self.__class__.__name__.replace("View", "Serializer")

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        serializer_name = self._get_serializer_name()
        return getattr(module, serializer_name)

    def get_paginated_response(self, data, headers=None):
        return self.paginator.get_paginated_response(data, headers)

    def check_throttles(self, request):
        throttle_durations = []
        for throttle in self.get_throttles():
            allowed = throttle.allow_request(request, self)
            if allowed is None:
                continue
            if not allowed:
                throttle_durations.append(throttle.wait())
            self.throttle_headers = throttle.get_headers()

        if throttle_durations:
            durations = [
                duration
                for duration in throttle_durations
                if duration is not None
            ]

            duration = max(durations, default=None)
            self.throttled(request, duration)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if hasattr(self, "throttle_headers"):
            for name, value in self.throttle_headers.items():
                response[name] = value
        return response
