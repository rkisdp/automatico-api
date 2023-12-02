from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from security.permissions import DefaultPasswordPermission

from ..serializers import ProfileSerializer

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, DefaultPasswordPermission]

    def get_queryset(self):
        pass

    def get_object(self):
        return self.request.user
