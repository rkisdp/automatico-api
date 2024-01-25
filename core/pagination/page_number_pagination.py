from collections import OrderedDict

from rest_framework.pagination import (
    PageNumberPagination as BasePageNumberPagination,
)
from rest_framework.response import Response

Link = str


class PageNumberPagination(BasePageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def _get_links(self) -> list[Link]:
        links = []
        for url, label in (
            (self.page.paginator.count, "count"),
            (self.get_first_link(), "first"),
            (self.get_previous_link(), "prev"),
            (self.get_next_link(), "next"),
            (self.get_last_link(), "last"),
        ):
            if url is not None:
                url = url.replace("/?", "?")
                links.append((url, label))

        return links

    def get_paginated_response(self, data):
        links = self._get_links()
        return Response(
            OrderedDict(
                *links,
                ("results", data),
            )
        )
