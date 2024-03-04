from rest_framework.renderers import JSONRenderer, zero_as_none
from rest_framework.utils.mediatypes import parse_header_parameters


class AutoMaticoJSONRenderer(JSONRenderer):
    media_type = "application/vnd.automatico+json"
    format = "automatico+json"

    def get_indent(self, accepted_media_type, renderer_context):
        """S"""
        if accepted_media_type:
            # If the media type looks like 'application/vnd.automatico+json;
            # indent=4', then pretty print the result.
            # Note that we coerce `indent=0` into `indent=None`.
            base_media_type, params = parse_header_parameters(
                accepted_media_type
            )
            try:
                return zero_as_none(max(min(int(params["indent"]), 8), 0))
            except (KeyError, ValueError, TypeError):
                pass

        return renderer_context.get("indent", 2)
