from importlib import import_module

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView

SCHEMA_TAGS = ("users",)


@extend_schema(tags=SCHEMA_TAGS)
class UserDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = get_user_model().objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
