from rest_framework import status
from rest_framework.mixins import UpdateModelMixin as BaseUpdateModelMixin
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class UpdateModelMixin(
    ETagLastModifiedMixin,
    BaseUpdateModelMixin,
):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        headers = self.get_headers(request, serializer.data, instance)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
