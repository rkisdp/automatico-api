from importlib import import_module

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from workshops.models import WorkshopContactModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopContactDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = WorkshopContactModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"

    @extend_schema(
        operation_id="retrieve_workshop_contact",
        description="Retrieve workshop contact",
        summary="Retrieve workshop contact by workshop and contact id",
        parameters=(
            OpenApiParameter(
                name="contact_id",
                description="Contact id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
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
                description="Contact id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
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
                description="Contact id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="workshop_id",
                description="Workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"workshops.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "WorkshopContactListSerializer")
