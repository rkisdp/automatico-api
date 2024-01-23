import os
import re

from drf_spectacular.drainage import (
    add_trace_message,
    error,
    get_override,
    warn,
)
from drf_spectacular.generators import SchemaGenerator as BaseSchemaGenerator
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import camelize_operation, modify_for_versioning
from drf_spectacular.settings import spectacular_settings

from core.exceptions import ApiVersionError


def operation_matches_version(view, requested_version):
    try:
        version = view.request.version
    except ApiVersionError:
        return False
    else:
        return str(version) == str(requested_version)


class SchemaGenerator(BaseSchemaGenerator):
    def parse(self, input_request, public):
        # Same as BaseSchemaGenerator.parse, but with skiping allowed versioning
        # classes and operation_matches_version check
        result = {}
        self._initialise_endpoints()
        endpoints = self._get_paths_and_endpoints()

        if spectacular_settings.SCHEMA_PATH_PREFIX is None:
            non_trivial_prefix = (
                len(set([view.__class__ for _, _, _, view in endpoints])) > 1
            )
            if non_trivial_prefix:
                path_prefix = os.path.commonpath(
                    [path for path, _, _, _ in endpoints]
                )
                path_prefix = re.escape(path_prefix)
            else:
                path_prefix = "/"
        else:
            path_prefix = spectacular_settings.SCHEMA_PATH_PREFIX
        if not path_prefix.startswith("^"):
            path_prefix = "^" + path_prefix

        for path, path_regex, method, view in endpoints:
            for w in get_override(view, "warnings", []):
                warn(w)
            for e in get_override(view, "errors", []):
                error(e)

            view.request = spectacular_settings.GET_MOCK_REQUEST(
                method, path, view, input_request
            )

            if not (public or self.has_view_permissions(path, method, view)):
                continue

            if view.versioning_class:
                version = (
                    self.api_version or view.versioning_class.default_version
                )
                if not version:
                    continue
                path = modify_for_versioning(
                    self.inspector.patterns, method, path, view, version
                )
                if not operation_matches_version(view, version):
                    continue

            assert isinstance(view.schema, AutoSchema), (
                f"Incompatible AutoSchema used on View {view.__class__}. Is DRF's "
                f'DEFAULT_SCHEMA_CLASS pointing to "drf_spectacular.openapi.AutoSchema" '
                f"or any other drf-spectacular compatible AutoSchema?"
            )
            with add_trace_message(getattr(view, "__class__", view)):
                operation = view.schema.get_operation(
                    path, path_regex, path_prefix, method, self.registry
                )

            if not operation:
                continue

            if spectacular_settings.SCHEMA_PATH_PREFIX_TRIM:
                path = re.sub(
                    pattern=path_prefix,
                    repl="",
                    string=path,
                    flags=re.IGNORECASE,
                )

            if spectacular_settings.SCHEMA_PATH_PREFIX_INSERT:
                path = spectacular_settings.SCHEMA_PATH_PREFIX_INSERT + path

            if not path.startswith("/"):
                path = "/" + path

            if spectacular_settings.CAMELIZE_NAMES:
                path, operation = camelize_operation(path, operation)

            result.setdefault(path, {})
            result[path][method.lower()] = operation

        return result
