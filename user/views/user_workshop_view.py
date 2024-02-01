from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class UserWorkshopView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    queryset = WorkshopModel.objects.none()
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-workshops-for-the-authenticated-user",
        summary="List workshops for the authenticated user",
        description=(
            "Lists workshops that the authenticated user is owner of."
            "\n\n"
            "**Note**: Pagination is powered exclusively by the `page` parameter. "
            "Use the [Link header]"
            "(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) "
            "to get the URL for the next page of workshops."
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create-a-workshop-for-the-authenticated-user",
        summary="Create a workshop for the authenticated user",
        description="Creates a workshop for the authenticated user.",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.workshops.all()

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "workshops")
        return getattr(module, "WorkshopListSerializer")
