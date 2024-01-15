from rest_framework import mixins
from rest_framework.generics import ListAPIView, get_object_or_404

from workshops.models import WorkshopContactModel, WorkshopModel
from workshops.serializers import (
    WorkshopContactDetailSerializer,
    WorkshopContactListSerializer,
)


class WorkshopContactListView(
    mixins.UpdateModelMixin,
    ListAPIView,
):
    serializer_class = WorkshopContactListSerializer
    lookup_field = "id"
    ordering = ("id",)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs.get("id")
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return WorkshopContactModel.objects.filter(workshop=workshop)

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return WorkshopContactDetailSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs.get("id")
        return context
