from rest_framework import status
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class ListModelMixin(ETagLastModifiedMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        etag = self.get_etag(request, str(queryset))
        if self.check_etag(request, etag):
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        serializer = self.get_serializer(queryset, many=True)
        headers = {"ETag": etag}
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
