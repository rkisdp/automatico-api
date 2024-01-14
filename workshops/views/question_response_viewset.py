from rest_framework.viewsets import ModelViewSet

from workshops.models import QuestionResponseModel
from workshops.serializers import QuestionResponseSerializer


class QuestionResponseViewSet(ModelViewSet):
    queryset = QuestionResponseModel.objects.all()
    serializer_class = QuestionResponseSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")
