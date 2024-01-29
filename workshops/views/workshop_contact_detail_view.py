from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from workshops.models import WorkshopContactModel

SCHEMA_TAGS = ("workshops", "deprecated")


@extend_schema(tags=SCHEMA_TAGS, deprecated=True)
class WorkshopContactDetailView(
    MultipleFieldLookupMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = WorkshopContactModel.objects.all()
    lookup_fields = ("workshop_id", "id")
    lookup_url_kwargs = ("workshop_id", "contact_id")

    @extend_schema(
        operation_id="retrieve_workshop_contact",
        description="Retrieve workshop contact",
        summary="Retrieve workshop contact by workshop and contact id",
        parameters=(
            OpenApiParameter(
                name="contact_id",
                description="The contact ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="update_workshop_contact",
        description="Update workshop contact",
        summary="Update workshop contact by workshop and contact id",
        parameters=(
            OpenApiParameter(
                name="contact_id",
                description="The contact ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete_workshop_contact",
        description="Delete workshop contact",
        summary="Delete workshop contact by workshop and contact id",
        parameters=(
            OpenApiParameter(
                name="contact_id",
                description="The contact ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "WorkshopContactListSerializer")
