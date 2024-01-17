from rest_framework.generics import ListCreateAPIView

from workshops.models import WorkshopModel
from workshops.serializers import WorkshopListSerializer


class WorkshopListView(ListCreateAPIView):
    queryset = WorkshopModel.objects.all()
    serializer_class = WorkshopListSerializer
    ordering = ("id",)
    filterset_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )
    search_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )
    ordering_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )
