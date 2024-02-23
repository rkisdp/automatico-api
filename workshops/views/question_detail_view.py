from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from questions.models import Question

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionDetailView(
    MultipleFieldLookupMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = Question.objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "question_number")

    @extend_schema(
        operation_id="retrieve-a-question",
        summary="Retrieve a question",
        description="Retrieves a question for a workshop",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="update-a-question",
        summary="Update a question",
        description="Updates a question for a workshop",
    )
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete-a-question",
        summary="Delete a question",
        description="Deletes a question for a workshop",
    )
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["workshop"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "questions")
        return getattr(module, "QuestionSerializer")
