from rest_framework import status
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class RetrieveModelMixin(ETagLastModifiedMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        etag = self.get_etag(request, str(serializer.data))
        last_modified = self.get_last_modified(request, instance)
        headers = {"ETag": etag}
        if last_modified is not None:
            headers["Last-Modified"] = last_modified
        if self.check_etag(request, etag) or self.check_last_modified(
            request, last_modified
        ):
            return Response(
                status=status.HTTP_304_NOT_MODIFIED,
                headers=headers,
            )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
