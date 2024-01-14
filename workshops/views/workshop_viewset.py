from rest_framework.viewsets import ModelViewSet

from workshops.models import WorkshopModel
from workshops.serializers import WorkshopSerializer


class WorkshopViewSet(ModelViewSet):
    queryset = WorkshopModel.objects.all()
    serializer_class = WorkshopSerializer
    lookup_field = "id"
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
