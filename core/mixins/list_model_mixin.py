from rest_framework import status
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class ListModelMixin(ETagLastModifiedMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        etag = self.get_etag(request, str(serializer.data))
        headers = {"ETag": etag}
        if self.check_etag(request, etag):
            return Response(
                status=status.HTTP_304_NOT_MODIFIED,
                headers=headers,
            )
        return self.get_paginated_response(serializer.data, headers=headers)
