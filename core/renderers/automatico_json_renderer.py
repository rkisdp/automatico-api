from rest_framework.renderers import JSONRenderer


class AutoMaticoJSONRenderer(JSONRenderer):
    media_type = "application/vnd.automatico+json"
    format = "automatico+json"
