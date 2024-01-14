from rest_framework.viewsets import ModelViewSet

from workshops.models import ReviewResponseModel
from workshops.serializers import ReviewResponseSerializer


class ReviewResponseViewSet(ModelViewSet):
    queryset = ReviewResponseModel.objects.all()
    serializer_class = ReviewResponseSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("review", "response")
    search_fields = ("review", "response")
    ordering_fields = ("review", "response")
