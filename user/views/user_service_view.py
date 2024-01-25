from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from core.generics import GenericAPIView
from services.models import ServiceModel

SCHEMA_TAGS = ("user",)


@extend_schema(tags=SCHEMA_TAGS)
class UserServiceView(
    mixins.ListModelMixin,
    GenericAPIView,
):
    queryset = ServiceModel.objects.none()
    permission_classes = (IsAuthenticated,)
    ordering = ("id",)
    ordering_fields = ("id", "start_date", "end_date")
    filterset_fields = ("histories__status__name",)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return ServiceModel.objects.filter(vehicle__owner=self.request.user)
