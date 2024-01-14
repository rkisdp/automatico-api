from rest_framework.viewsets import ModelViewSet

from workshops.models import SpecialityModel
from workshops.serializers import SpecialitySerializer


class SpecialityViewSet(ModelViewSet):
    queryset = SpecialityModel.objects.all()
    serializer_class = SpecialitySerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)
