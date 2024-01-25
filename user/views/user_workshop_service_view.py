from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from services.models import ServiceModel

SCHEMA_TAGS = ("user",)


@extend_schema(tags=SCHEMA_TAGS)
class UserWorkshopServiceView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    permission_classes = (IsAuthenticated,)
    queryset = ServiceModel.objects.none()
    ordering = ("id",)
    ordering_fields = ("id", "start_date", "end_date")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return ServiceModel.objects.filter(workshop__owner=self.request.user)
