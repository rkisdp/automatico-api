import hashlib

from django.core.cache import cache
from django.utils.http import http_date


class ETagLastModifiedMixin:
    def get_last_modified(self, request, obj):
        if not hasattr(obj, "updated_at"):
            return None

        last_modified = http_date(obj.updated_at.timestamp())
        cache_key_last_modified = f"{request.path}-last-modified"
        cache.set(cache_key_last_modified, last_modified, timeout=None)
        return last_modified

    def get_etag(self, request, data):
        etag = hashlib.sha256(str(data).encode("utf-8")).hexdigest()
        cache_key = f"{request.path}-etag"
        cache.set(cache_key, etag, timeout=None)
        return f'"{etag}"'

    def check_etag(self, request, etag):
        if_none_match = request.headers.get("If-None-Match")
        if etag is None or if_none_match is None:
            return False
        return if_none_match == etag

    def check_last_modified(self, request, last_modified):
        if_modified_since = request.headers.get("If-Modified-Since")
        if last_modified is None or if_modified_since is None:
            return False
        return if_modified_since == last_modified
