from rest_framework.viewsets import ModelViewSet

from workshops.models import ReviewModel
from workshops.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)
    lookup_field = "id"
