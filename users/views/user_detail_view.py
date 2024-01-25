from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
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

    @extend_schema(
        operation_id="get-a-user",
        summary="Get a user",
        description=(
            "Provides publicly available information about someone with an "
            "AutoMático account."
        ),
        parameters=(
            OpenApiParameter(
                name="user_id",
                description="The user ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
