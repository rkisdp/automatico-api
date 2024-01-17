from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from workshops.models import SpecialityModel
from workshops.serializers import SpecialitySerializer


class SpecialityViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = SpecialityModel.objects.all()
    serializer_class = SpecialitySerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)
