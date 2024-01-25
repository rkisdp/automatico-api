from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = WorkshopModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"

    @extend_schema(
        operation_id="get-a-workshop",
        summary="Get a workshop",
        description=(
            "Provides publicly available information about an "
            "AutoMático workshop."
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="update-a-workshop",
        summary="Update a workshop",
        description=(
            "Updates a workshop. The authenticated user must be the owner of "
            "the workshop."
            "\n\n"
            "**Note**: To edit a workshop's brands, contacts, employees or "
            "specialities use the corresponding endpoints."
            "\n\n"
            "### Swagger endpoints:"
            "\n\n"
            "- [Replace all workshop brands]"
            "(/documentation/swagger#workshops/update_workshop_brands)"
            "\n\n"
            "- [Replace all workshop contacts]"
            "(/documentation/swagger#workshops/update_workshop_contacts)"
            "\n\n"
            "- [Replace all workshop employees]"
            "(/documentation/swagger#workshops/update_workshop_employees)"
            "\n\n"
            "- [Replace all workshop specialities]"
            "(/documentation/swagger#workshops/update_workshop_specialities)"
            "\n\n"
            "### Redoc endpoints:"
            "\n\n"
            "- [Replace all workshop brands]"
            "(/documentation/redoc#tag/workshops/operation/replace_all_workshop_brands)"
            "\n\n"
            "- [Replace all workshop contacts]"
            "(/documentation/redoc#tag/workshops/operation/replace_all_workshop_contacts)"
            "\n\n"
            "- [Replace all workshop employees]"
            "(/documentation/redoc#tag/workshops/operation/replace_all_workshop_employees)"
            "\n\n"
            "- [Replace all workshop specialities]"
            "(/documentation/redoc#tag/workshops/operation/replace_all_workshop_specialities)"
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="deactivate-a-workshop",
        summary="Deactivate a workshop",
        description=(
            "Deactivates a workshop. The authenticated user must be the owner "
            "of the workshop."
            "\n\n"
            "**Note**: Deactivated workshops cannot receive nor accept new "
            "service requests."
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop id.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        if not instance.is_active:
            return
        instance.is_active = False
        instance.save()
