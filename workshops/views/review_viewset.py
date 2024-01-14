from rest_framework.viewsets import ModelViewSet

from workshops.models import ReviewModel
from workshops.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)
