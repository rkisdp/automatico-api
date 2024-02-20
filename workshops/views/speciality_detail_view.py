from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
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
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
