from rest_framework.viewsets import ModelViewSet

from workshops.models import QuestionModel
from workshops.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("workshop", "question")
    search_fields = ("workshop", "question")
    ordering_fields = ("workshop", "question")
