from rest_framework.generics import ListAPIView

from workshops.models import SpecialityModel
from workshops.serializers import SpecialitySerializer


class SpecialityView(ListAPIView):
    queryset = SpecialityModel.objects.all()
    serializer_class = SpecialitySerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)
