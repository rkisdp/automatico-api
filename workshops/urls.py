from rest_framework.routers import DefaultRouter

from . import views

app_name = "workshops"

router = DefaultRouter()
router.register("workshops", views.WorkshopViewSet, basename="workshops")
router.register(
    "workshops/contacts",
    views.WorkshopContactViewSet,
    basename="workshop-contacts",
)
router.register(
    "specialities", views.SpecialityViewSet, basename="specialities"
)
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

urlpatterns = []

urlpatterns += router.urls
