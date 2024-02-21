from rest_framework import status
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class RetrieveModelMixin(ETagLastModifiedMixin):
    def retrieve(self, request, *args, **kwargs):
        if self.check_etag(request) or self.check_last_modified(request):
            headers = self.get_headers_from_cache(request)
            return Response(
                status=status.HTTP_304_NOT_MODIFIED,
                headers=headers,
            )
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        headers = self.get_headers(request, serializer.data, instance)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
