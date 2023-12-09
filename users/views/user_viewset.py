from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..serializers import UserSerializer

SCHEMA_NAME = "users"


@extend_schema(tags=[SCHEMA_NAME])
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    ordering = ["id"]
    ordering_fields = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
