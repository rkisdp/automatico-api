from rest_framework.parsers import JSONParser

from core.renderers import AutoMaticoJSONRenderer


class AutoMaticoJSONParser(JSONParser):
    """
    vnd.automatico+json parser.
    """

    media_type = "application/vnd.automatico+json"
    renderer_class = AutoMaticoJSONRenderer
