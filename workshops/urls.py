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

urlpatterns = (
    path(
        "",
        views.WorkshopListView.as_view(),
        name="list",
    ),
    path(
        "<int:id>/",
        views.WorkshopDetailView.as_view(),
        name="detail",
    ),
    path(
        "<int:id>/contacts/",
        views.WorkshopContactListView.as_view(),
        name="contacts-list",
    ),
    path(
        "<int:id>/brands/",
        views.WorkshopBrandListView.as_view(),
        name="brands-list",
    ),
    path(
        "<int:id>/specialities/",
        views.WorkshopSpecialityListView.as_view(),
        name="specialities-list",
    ),
    path(
        "<int:id>/vehicles/",
        views.WorkshopVehicleListView.as_view(),
        name="vehicles-list",
    ),
    path(
        "<int:id>/employees/",
        views.WorkshopEmployeeListView.as_view(),
        name="employees-list",
    ),
    path(
        "specialities/",
        views.SpecialityView.as_view(),
        name="specialities",
    ),
)
