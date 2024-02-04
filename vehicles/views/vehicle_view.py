from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from vehicles.models import VehicleModel

SCHEMA_TAGS = ("vehicles",)


@extend_schema(tags=SCHEMA_TAGS)
class VehicleView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = VehicleModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "vehicle_id"

    @extend_schema(
        operation_id="get-a-vehicle",
        summary="Get a vehicle",
        description=(
            "Provides publicly available information about a vehicle."
        ),
        parameters=(
            OpenApiParameter(
                name="vehicle_id",
                description="The vehicle ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="update-a-vehicle",
        summary="Update a vehicle",
        description=(
            "Updates a vehicle. The authenticated user must be the owner of "
            "the vehicle."
        ),
        parameters=(
            OpenApiParameter(
                name="vehicle_id",
                description="The vehicle ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, partial=True, *args, **kwargs)

    # @extend_schema(
    #     operation_id="delete-a-vehicle",
    #     summary="Delete a vehicle",
    #     description=(
    #         "Deletes a vehicle. The authenticated user must be the owner of "
    #         "the vehicle."
    #     ),
    #     deprecated=True,
    #     tags=(*SCHEMA_TAGS, "deprecated"),
    #     parameters=(
    #         OpenApiParameter(
    #             name="vehicle_id",
    #             description="The vehicle ID.",
    #             type=OpenApiTypes.INT,
    #             location=OpenApiParameter.PATH,
    #             required=True,
    #         ),
    #     ),
    # )
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
