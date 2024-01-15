from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from workshops.models import ReviewPhotoModel
from workshops.serializers import ReviewPhotoSerializer


class ReviewPhotoViewSet(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = ReviewPhotoModel.objects.all()
    serializer_class = ReviewPhotoSerializer
    lookup_field = "id"
    ordering = ("id",)
    filterset_fields = ("review",)
    search_fields = ("review",)
    ordering_fields = ("review",)
