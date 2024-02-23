from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from core import mixins
from core.generics import GenericAPIView
from workshops.models import Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class UserFavoriteWorkshopListView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    queryset = Workshop.objects.none()
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-favorite-workshops-for-the-authenticated-user",
        summary="List favorite workshops for the authenticated user",
        description=(
            "Lists favorite workshops that the authenticated user is owner of."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
    )
    @method_decorator(cache_control(private=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.favorite_workshops.all()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "workshops")
        return getattr(module, "MinimalWorkshopSerializer")
