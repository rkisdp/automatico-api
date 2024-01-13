from rest_framework.viewsets import ModelViewSet

from workshops.models import QuestionResponseModel
from workshops.serializers import QuestionResponseSerializer


class QuestionResponseViewSet(ModelViewSet):
    queryset = QuestionResponseModel.objects.all()
    serializer_class = QuestionResponseSerializer
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")
    lookup_field = "id"
