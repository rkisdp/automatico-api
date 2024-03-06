from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from core import mixins
from core.generics import GenericAPIView

SCHEMA_TAGS = ("users",)


@extend_schema(tags=SCHEMA_TAGS)
class UserDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = get_user_model().global_objects.all()
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
    @method_decorator(cache_control(private=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
