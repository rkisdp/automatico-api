from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from core import mixins
from core.generics import GenericAPIView, get_object_or_404
from vehicles.models import VehicleBrand
from workshops.models import Workshop

SCHEMA_TAGS = ("workshops",)


@extend_schema(tags=SCHEMA_TAGS)
class WorkshopBrandListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView,
):
    queryset = VehicleBrand.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    ordering_fields = ("id", "name")

    @extend_schema(
        operation_id="list-workshop-brands",
        summary="List workshop brands",
        description="Lists the brands that a workshop works with.",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
            OpenApiParameter(
                name="ordering",
                description="Which field to use when ordering the results.",
                type=OpenApiTypes.STR,
                many=True,
                explode=False,
                enum=(
                    field
                    for pair in zip(
                        ordering_fields,
                        (f"-{field}" for field in ordering_fields),
                    )
                    for field in pair
                ),
                default="id",
            ),
            OpenApiParameter(
                name="page",
                description="The page number of the results to fetch.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=1,
            ),
            OpenApiParameter(
                name="page_size",
                description="The number of results to return per page (max 100)..",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                default=api_settings.PAGE_SIZE,
            ),
        ),
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="add-brands-to-a-workshop",
        summary="Add brands to a workshop",
        description="Adds brands that a workshop works with.",
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="replace-all-workshop-brands",
        summary="Replace all workshop brands",
        description=(
            "Replaces all brands that a workshop works with. This will remove "
            "all existing brands and add the new ones."
            "\n\n"
            "If you pass an empty list, it will remove all brands."
        ),
        parameters=(
            OpenApiParameter(
                name="workshop_id",
                description="The workshop ID.",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
            ),
        ),
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(Workshop.global_objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return self.queryset.filter(workshop_brands=workshop)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        if self.request.method in ("POST", "PUT"):
            return getattr(module, "WorkshopBrandDetailSerializer")
        return getattr(module, self._get_serializer_name())
