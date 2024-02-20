from rest_framework import status
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class ListModelMixin(ETagLastModifiedMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        headers = self.get_headers(request, serializer.data)
        if self.check_etag(request):
            return Response(
                status=status.HTTP_304_NOT_MODIFIED,
                headers=headers,
            )
        return self.get_paginated_response(serializer.data, headers=headers)
