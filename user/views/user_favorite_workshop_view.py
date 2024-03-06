from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core import mixins
from core.generics import GenericAPIView
from workshops.models import Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class UserFavoriteWorkshopView(
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    queryset = Workshop.global_objects.all()
    ordering = ("id",)
    ordering_fields = ("id", "name")
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"

    @extend_schema(
        operation_id="add-workshop-to-favorite-for-the-authenticated-user",
        summary="Add workshop to favorite for the authenticated user",
        description=("Adds a workshop to favorite for the authenticated user."),
        responses={204: None},
    )
    def put(self, request, *args, **kwargs):
        workshop = self.get_object()
        request.user.favorite_workshops.add(workshop)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        operation_id="remove-favorite-workshop-for-the-authenticated-user",
        summary="Remove favorite workshop for the authenticated user",
        description=("Removes a favorite workshop for the authenticated user."),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        self.request.user.favorite_workshops.remove(instance)
