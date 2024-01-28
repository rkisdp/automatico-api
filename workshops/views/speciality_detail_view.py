from drf_spectacular.utils import extend_schema
from rest_framework import mixins

from core.generics import GenericAPIView
from workshops.models import SpecialityModel

SCHEMA_TAGS = ("workshops", "deprecated")


@extend_schema(tags=SCHEMA_TAGS)
class SpecialityDetailView(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):
    queryset = SpecialityModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "speciality_id"

    @extend_schema(
        operation_id="retrieve_specialities",
        description="Retrieve all specialities",
        summary="Retrieve all specialities",
        deprecated=True,
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
