from rest_framework import serializers

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


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopModel
        fields = (
            "id",
            "owner",
            "name",
            "latitude",
            "longitude",
            "employees",
            "specialities",
            "vehicles",
        )
        read_only_fields = ("id",)


class WorkshopContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopContactModel
        fields = ("id", "workshop", "name", "value")
        read_only_fields = ("id",)


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityModel
        fields = ("id", "name")
        read_only_fields = ("id",)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ("id", "workshop", "question")
        read_only_fields = ("id",)


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponseModel
        fields = ("id", "question", "response")
        read_only_fields = ("id",)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ("id", "workshop")
        read_only_fields = ("id",)


class ReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPhotoModel
        fields = ("id", "review")
        read_only_fields = ("id",)


class ReviewResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewResponseModel
        fields = ("id", "review", "response")
        read_only_fields = ("id",)


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponseModel
        fields = ("id", "question", "response")
        read_only_fields = ("id",)


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponseModel
        fields = ("id", "question", "response")
        read_only_fields = ("id",)
