from __future__ import annotations

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param, replace_query_param

LinkHeader = str


class HeaderPagination(PageNumberPagination):
    """Header based pagination

    Pagination metadata are specified in response's headers.
    Information about pagination is provided in the Link header.

    Headers:
    --------
    X-Page-Count: Total page count
    X-Current-Page: Current page number
    X-Page-Size: Item count in the current page
    X-Total: Total number of item included if `include_count` is `True`

    Link: previous, next, first & last links.
          See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link

    Parameters
    ----------
    include_count: Include result set count in `X-Total` header.
    """

    page_size_query_param = "page_size"
    include_count = True
    page_size = 25
    max_page_size = 100

    def _get_links(self) -> list[LinkHeader]:
        links = []
        for url, label in (
            (self.get_first_link(), "first"),
            (self.get_previous_link(), "prev"),
            (self.get_next_link(), "next"),
            (self.get_last_link(), "last"),
        ):
            if url is not None:
                url = url.replace("/?", "?")
                links.append(f"<{url}>; rel='{label}'")

        return links

    def get_paginated_response(self, data) -> Response:
        links = self._get_links()

        headers = {
            "X-Page-Count": self.page.paginator.num_pages,
            "X-Page-Size": self.page_size,
            "X-Current-Page": self.page.number,
        }

        if self.include_count:
            headers.update({"X-Total": self.page.paginator.count})

        if links:
            headers.update({"Link": ", ".join(links)})

        return Response(data, headers=headers)

    def get_first_link(self) -> str | None:
        if not self.page.has_previous():
            return None

        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.page_query_param)

    def get_last_link(self) -> str | None:
        if not self.page.has_next():
            return None

        url = self.request.build_absolute_uri()
        return replace_query_param(
            url,
            self.page_query_param,
            self.page.paginator.num_pages,
        )

    def get_paginated_response_schema(self, schema: dict) -> dict:
        return schema
