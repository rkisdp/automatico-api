from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "workshops"

router = DefaultRouter(trailing_slash=False)
router.register(
    "/questions",
    views.QuestionViewSet,
    basename="questions",
)
router.register(
    "/questions/responses",
    views.QuestionResponseViewSet,
    basename="question-responses",
)
router.register(
    "/reviews",
    views.ReviewViewSet,
    basename="reviews",
)
router.register(
    "/reviews/photos",
    views.ReviewPhotoViewSet,
    basename="review-photos",
)
router.register(
    "/reviews/responses",
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
        "/<int:workshop_id>",
        views.WorkshopDetailView.as_view(),
        name="detail",
    ),
    path(
        "/<int:workshop_id>/brands",
        views.WorkshopBrandListView.as_view(),
        name="brands",
    ),
    path(
        "/<int:workshop_id>/contacts",
        views.WorkshopContactListView.as_view(),
        name="contacts",
    ),
    path(
        "/<int:workshop_id>/employees",
        views.WorkshopEmployeeListView.as_view(),
        name="employees",
    ),
    path(
        "/<int:workshop_id>/services",
        views.WorkshopServiceView.as_view(),
        name="services",
    ),
    path(
        "/<int:workshop_id>/specialities",
        views.WorkshopSpecialityListView.as_view(),
        name="specialities",
    ),
    path(
        "/<int:workshop_id>/vehicles",
        views.WorkshopVehicleView.as_view(),
        name="vehicles",
    ),
    path(
        "/<int:workshop_id>/contacts/<int:contact_id>",
        views.WorkshopContactDetailView.as_view(),
        name="contact-detail",
    ),
    path(
        "/specialities",
        views.SpecialityListView.as_view(),
        name="speciality-list",
    ),
    path(
        "/specialities/<int:speciality_id>",
        views.SpecialityDetailView.as_view(),
        name="speciality-detail",
    ),
)

urlpatterns += (*router.urls,)
