from rest_framework.viewsets import ModelViewSet

from workshops.models import ReviewPhotoModel
from workshops.serializers import ReviewPhotoSerializer


class ReviewPhotoViewSet(ModelViewSet):
    queryset = ReviewPhotoModel.objects.all()
    serializer_class = ReviewPhotoSerializer
    filterset_fields = ("review",)
    search_fields = ("review",)
    ordering_fields = ("review",)
    lookup_field = "id"
