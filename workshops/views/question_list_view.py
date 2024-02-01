from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from core.generics import GenericAPIView
from workshops.models import WorkshopModel

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    lookup_field = "id"
    lookup_url_kwarg = "workshop_id"
    ordering = ("id",)
    ordering_fields = ("workshop", "question")

    @extend_schema(
        operation_id="List questions",
        description="List questions",
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="Create question",
        description="Create question",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_object(self):
        workshop_id = self.kwargs[self.lookup_url_kwarg]
        return get_object_or_404(WorkshopModel.objects.all(), id=workshop_id)

    def get_queryset(self):
        workshop = self.get_object()
        return workshop.questions.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop_id"] = self.kwargs[self.lookup_url_kwarg]
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "questions")
        return getattr(module, "QuestionSerializer")
