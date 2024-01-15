from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "workshops"

router = DefaultRouter()
router.register("questions", views.QuestionViewSet, basename="questions")
router.register(
    "questions/responses",
    views.QuestionResponseViewSet,
    basename="question-responses",
)
router.register("reviews", views.ReviewViewSet, basename="reviews")
router.register(
    "reviews/photos", views.ReviewPhotoViewSet, basename="review-photos"
)
router.register(
    "reviews/responses",
    views.ReviewResponseViewSet,
    basename="review-responses",
)
router.register("", views.WorkshopViewSet, basename="workshops")

urlpatterns = (
    path(
        "",
        views.WorkshopViewSet.as_view({"get": "list", "post": "create"}),
        name="workshops",
    ),
    path(
        "<int:id>/contacts/",
        views.WorkshopContactListView.as_view(),
        name="contacts-list",
    ),
    path(
        "<int:id>/specialities/",
        views.WorkshopContactListView.as_view(),
        name="specialities-list",
    ),
    path(
        "<int:id>/vehicles/",
        views.WorkshopContactListView.as_view(),
        name="vehicles-list",
    ),
    path(
        "<int:id>/employees/",
        views.WorkshopContactListView.as_view(),
        name="employees-list",
    ),
    path(
        "specialities/",
        views.SpecialityView.as_view(),
        name="specialities",
    ),
)
