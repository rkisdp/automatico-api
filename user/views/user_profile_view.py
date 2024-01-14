from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView

from user.serializers import ProfileSerializer

SCHEMA_NAME = "user"


@extend_schema(tags=[SCHEMA_NAME])
class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
