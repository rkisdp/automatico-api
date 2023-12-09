from rest_framework.viewsets import ModelViewSet

from workshops.models import (
    QuestionModel,
    QuestionResponseModel,
    ReviewModel,
    ReviewPhotoModel,
    ReviewResponseModel,
    SpecialityModel,
    WorkshopContactModel,
    WorkshopModel,
)
from workshops.serializers import (
    QuestionResponseSerializer,
    QuestionSerializer,
    ReviewPhotoSerializer,
    ReviewResponseSerializer,
    ReviewSerializer,
    SpecialitySerializer,
    WorkshopContactSerializer,
    WorkshopSerializer,
)


class WorkshopViewSet(ModelViewSet):
    queryset = WorkshopModel.objects.all()
    serializer_class = WorkshopSerializer
    filterset_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )
    search_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )
    ordering_fields = (
        "owner",
        "name",
        "latitude",
        "longitude",
        "employees",
        "specialities",
        "vehicles",
    )


class WorkshopContactViewSet(ModelViewSet):
    queryset = WorkshopContactModel.objects.all()
    serializer_class = WorkshopContactSerializer
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)


class SpecialityViewSet(ModelViewSet):
    queryset = SpecialityModel.objects.all()
    serializer_class = SpecialitySerializer
    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)


class ReviewViewSet(ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ("workshop",)
    search_fields = ("workshop",)
    ordering_fields = ("workshop",)


class ReviewPhotoViewSet(ModelViewSet):
    queryset = ReviewPhotoModel.objects.all()
    serializer_class = ReviewPhotoSerializer
    filterset_fields = ("review",)
    search_fields = ("review",)
    ordering_fields = ("review",)


class ReviewResponseViewSet(ModelViewSet):
    queryset = ReviewResponseModel.objects.all()
    serializer_class = ReviewResponseSerializer
    filterset_fields = ("review", "response")
    search_fields = ("review", "response")
    ordering_fields = ("review", "response")


class QuestionViewSet(ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ("workshop", "question")
    search_fields = ("workshop", "question")
    ordering_fields = ("workshop", "question")


class QuestionResponseViewSet(ModelViewSet):
    queryset = QuestionResponseModel.objects.all()
    serializer_class = QuestionResponseSerializer
    filterset_fields = ("question", "response")
    search_fields = ("question", "response")
    ordering_fields = ("question", "response")
