from rest_framework.generics import ListCreateAPIView

from workshops.models import WorkshopModel
from workshops.serializers import WorkshopListSerializer


class WorkshopListView(ListCreateAPIView):
    queryset = WorkshopModel.objects.all()
    serializer_class = WorkshopListSerializer
    ordering = ("id",)
    filterset_fields = ("specialities__name", "brands__name")
    search_fields = (
        "name",
        "specialities__name",
        "brands__name",
    )
    ordering_fields = ("name",)
