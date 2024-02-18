from rest_framework import status
from rest_framework.mixins import CreateModelMixin as BaseCreateModelMixin
from rest_framework.response import Response

from .etag_last_modified_mixin import ETagLastModifiedMixin


class CreateModelMixin(
    ETagLastModifiedMixin,
    BaseCreateModelMixin,
):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data, serializer.instance)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def get_success_headers(self, data, instance):
        headers = super().get_success_headers(data)
        headers["ETag"] = self.get_etag(self.request, str(data))
        headers["Last-Modified"] = self.get_last_modified(
            self.request,
            instance,
        )
        return headers
