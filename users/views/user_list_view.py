from importlib import import_module

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView

SCHEMA_NAME = "users"


@extend_schema(tags=[SCHEMA_NAME])
class UserListView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = get_user_model().objects.all()
    ordering = ("id",)
    ordering_fields = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
