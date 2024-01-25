from importlib import import_module

from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from services.models import ServiceHistoryModel, ServiceModel


class ServiceHistoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = ServiceHistoryModel.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "service_id"
    ordering = ("id",)
    filterset_fields = ("service", "status")

    def get_object(self):
        service_id = self.kwargs.get("id")
        return get_object_or_404(ServiceModel.objects.all(), id=service_id)

    def get_queryset(self):
        service = self.get_object()
        return ServiceHistoryModel.objects.filter(service=service)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["service_id"] = self.kwargs.get("id")
        return context

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = import_module(
            f"services.serializers.{version.replace('.', '_')}"
        )
        return getattr(module, "ServiceHistorySerializer")
