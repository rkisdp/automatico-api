import hashlib

from django.core.cache import cache
from django.utils.http import http_date, parse_http_date_safe
from django.utils.translation import gettext_lazy as _

from core.exceptions import PreconditionFailed


class ETagLastModifiedMixin:
    def get_headers(self, request, data, obj=None) -> dict:
        etag = self._set_etag(request, str(data))
        if obj is not None:
            last_modified = self._set_last_modified(request, obj)
        headers = {"ETag": etag}
        if "last_modified" in locals() and last_modified is not None:
            headers["Last-Modified"] = last_modified
        return headers

    def get_headers_from_cache(self, request) -> dict:
        etag = cache.get(f"{request.path}-etag")
        last_modified = cache.get(f"{request.path}-last-modified")
        headers = {"ETag": etag}
        if last_modified is not None:
            headers["Last-Modified"] = last_modified
        return headers

    def _set_last_modified(self, request, obj) -> str | None:
        if not hasattr(obj, "updated_at"):
            return None

        last_modified = http_date(obj.updated_at.timestamp())
        request_path = (
            request.path
            if not request.path.endswith("/")
            else request.path[:-1]
        )
        cache_key_last_modified = f"{request_path}-last-modified"
        cache.set(cache_key_last_modified, last_modified, timeout=None)
        return last_modified

    def _set_etag(self, request, data: str) -> str:
        etag = hashlib.sha256(data.encode("utf-8")).hexdigest()
        etag = f'W/"{etag}"'
        request_path = (
            request.path
            if not request.path.endswith("/")
            else request.path[:-1]
        )
        cache_key = f"{request_path}-etag"
        cache.set(cache_key, etag, timeout=None)
        return etag

    def check_etag(self, request) -> bool:
        if request.headers.get("If-Match", None) is not None:
            return self._check_if_match(request)
        if request.headers.get("If-None-Match", None) is not None:
            return self._check_if_none_match(request)
        return False

    def check_last_modified(self, request) -> bool:
        if request.headers.get("If-Modified-Since", None) is not None:
            return self._check_if_modified_since(request)
        if request.headers.get("If-Unmodified-Since", None) is not None:
            return self._check_if_unmodified_since(request)
        return False

    def _check_if_match(self, request) -> bool:
        if_match = request.headers.get("If-Match")
        if if_match is None:
            return False

        cache_key = f"{request.path}-etag"
        etag = cache.get(cache_key)
        if etag not in if_match.split(", "):
            raise PreconditionFailed(
                detail=_(
                    "The entity tag provided in the request does not match the "
                    "entity tag of the resource."
                )
            )
        return True

    def _check_if_none_match(self, request) -> bool:
        cache_key = f"{request.path}-etag"
        etag = cache.get(cache_key)

        if_none_match = request.headers.get("If-None-Match")
        if request.method in ("GET", "HEAD"):
            return etag in if_none_match.split(", ")

        if request.method in (
            "PUT",
            "PATCH",
            "DELETE",
        ) and etag in if_none_match.split(", "):
            raise PreconditionFailed(
                detail=_(
                    "The entity tag provided in the request does not match "
                    "the entity tag of the resource."
                )
            )
        return False

    def _check_if_modified_since(self, request) -> bool:
        if_modified_since = request.headers.get("If-Modified-Since")
        if_modified_since = parse_http_date_safe(if_modified_since)
        if if_modified_since is None:
            return False

        cache_key = f"{request.path}-last-modified"
        last_modified = cache.get(cache_key)
        last_modified = parse_http_date_safe(last_modified)
        if last_modified is None:
            return False
        return if_modified_since >= last_modified

    def _check_if_unmodified_since(self, request) -> bool:
        if_unmodified_since = request.headers.get("If-Unmodified-Since")
        if_unmodified_since = parse_http_date_safe(if_unmodified_since)
        if if_unmodified_since is None:
            return False

        cache_key = f"{request.path}-last-modified"
        last_modified = cache.get(cache_key)
        last_modified = parse_http_date_safe(last_modified)
        if last_modified is None:
            return False

        if if_unmodified_since < last_modified:
            raise PreconditionFailed(
                detail=_(
                    "The resource has been modified after the date specified "
                    "in the If-Unmodified-Since header."
                )
            )
        return True
