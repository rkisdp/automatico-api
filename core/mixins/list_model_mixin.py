from rest_framework import status
from rest_framework.mixins import ListModelMixin as BaseListModelMixin
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class ListModelMixin(ETagLastModifiedMixin, BaseListModelMixin):
    def list(self, request, *args, **kwargs):
        if self.check_etag(request):
            headers = self.get_headers_from_cache(request)
            return Response(
                status=status.HTTP_304_NOT_MODIFIED,
                headers=headers,
            )
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        headers = self.get_headers(request, serializer.data)
        return self.get_paginated_response(serializer.data, headers=headers)
