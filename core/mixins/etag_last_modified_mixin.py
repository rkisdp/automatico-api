import hashlib

from django.core.cache import cache
from django.utils.http import http_date, parse_http_date_safe
from django.utils.translation import gettext_lazy as _

from core.exceptions import PreconditionFailed


class ETagLastModifiedMixin:
    def get_last_modified(self, request, obj) -> str:
        if not hasattr(obj, "updated_at"):
            return None

        last_modified = http_date(obj.updated_at.timestamp())
        cache_key_last_modified = f"{request.path}-last-modified"
        cache.set(cache_key_last_modified, last_modified, timeout=None)
        return last_modified

    def get_etag(self, request, data: str) -> str:
        etag = hashlib.sha256(data.encode("utf-8")).hexdigest()
        cache_key = f"{request.path}-etag"
        cache.set(cache_key, etag, timeout=None)
        return f'W/"{etag}"'

    def check_etag(self, request, etag) -> bool:
        if request.headers.get("If-Match", None) is not None:
            return self._check_if_match(request, etag)
        if request.headers.get("If-None-Match", None) is not None:
            return self._check_if_none_match(request, etag)
        return False

    def check_last_modified(self, request, last_modified) -> bool:
        if request.headers.get("If-Modified-Since", None) is not None:
            return self._check_if_modified_since(request, last_modified)
        if request.headers.get("If-Unmodified-Since", None) is not None:
            return self._check_if_unmodified_since(request, last_modified)
        return False

    def _check_if_match(self, request, etag) -> bool:
        if_match = request.headers.get("If-Match")
        if if_match is None:
            return False

        if etag not in if_match.split(", "):
            raise PreconditionFailed(
                detail=_(
                    "The entity tag provided in the request does not match the "
                    "entity tag of the resource."
                )
            )
        return True

    def _check_if_none_match(self, request, etag) -> bool:
        if_none_match = request.headers.get("If-None-Match")
        if if_none_match is None:
            return False

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

    def _check_if_modified_since(self, request, last_modified) -> bool:
        if_modified_since = request.headers.get("If-Modified-Since")
        if last_modified is None:
            return False

        if_modified_since_client = parse_http_date_safe(if_modified_since)
        if if_modified_since_client is None:
            return False

        if_modified_since_server = parse_http_date_safe(last_modified)
        return if_modified_since_client >= if_modified_since_server

    def _check_if_unmodified_since(self, request, last_modified) -> bool:
        if_unmodified_since = request.headers.get("If-Unmodified-Since")
        if last_modified is None:
            return False

        if_unmodified_since_client = parse_http_date_safe(if_unmodified_since)
        if if_unmodified_since_client is None:
            return False

        if_unmodified_since_server = parse_http_date_safe(last_modified)
        if if_unmodified_since_server is None:
            return False

        if if_unmodified_since_client < if_unmodified_since_server:
            raise PreconditionFailed(
                detail=_(
                    "The resource has been modified after the date specified "
                    "in the If-Unmodified-Since header."
                )
            )
        return True
