from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from drf_spectacular.utils import extend_schema

from core import mixins
from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from questions.models import Question

SCHEMA_TAGS = ("questions",)


@extend_schema(tags=SCHEMA_TAGS)
class QuestionResponseListView(
    MultipleFieldLookupMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    queryset = Question.objects.all()
    lookup_fields = ("workshop_id", "number")
    lookup_url_kwargs = ("workshop_id", "question_number")
    ordering = ("id",)
    search_fields = ("body",)
    ordering_fields = ("id",)

    @extend_schema(
        operation_id="list-a-question-answers",
        summary="List a question answers",
        description="Lists a question answers",
    )
    @method_decorator(cache_control(public=True, max_age=60, s_maxage=60))
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        operation_id="answer-a-question",
        summary="Answer a question",
        description="Answers a question",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        question = self.get_object()
        return question.answers.all().filter(is_deleted=False)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["question"] = self.get_object()
        return context

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version, "questions")
        return getattr(module, "QuestionResponseSerializer")
