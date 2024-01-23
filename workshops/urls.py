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
        "/<int:workshop_id>/contacts",
        views.WorkshopContactListView.as_view(),
        name="contacts",
    ),
    path(
        "/<int:workshop_id>/brands",
        views.WorkshopBrandListView.as_view(),
        name="brands",
    ),
    path(
        "/<int:workshop_id>/employees",
        views.WorkshopEmployeeListView.as_view(),
        name="employees",
    ),
    path(
        "/<int:workshop_id>/services",
        views.WorkshopServiceViewSet.as_view({"get": "list", "post": "create"}),
        name="services",
    ),
    path(
        "/<int:workshop_id>/specialities",
        views.WorkshopSpecialityListView.as_view(
            {"get": "list", "put": "update"}
        ),
        name="specialities",
    ),
    path(
        "/<int:workshop_id>/vehicles",
        views.WorkshopVehicleViewSet.as_view({"get": "list", "put": "update"}),
        name="vehicles",
    ),
    path(
        "/specialities",
        views.SpecialityViewSet.as_view({"get": "list"}),
        name="speciality-list",
    ),
    path(
        "/<int:workshop_id>/contacts/<int:contact_id>",
        views.WorkshopContactDetailView.as_view(),
        name="contact-detail",
    ),
    path(
        "/contacts/<int:contact_id>",
        views.SpecialityViewSet.as_view({"get": "retrieve"}),
        name="contact-detail",
    ),
    path(
        "/specialities/<int:speciality_id>",
        views.SpecialityViewSet.as_view({"get": "retrieve"}),
        name="speciality-detail",
    ),
)

urlpatterns += (*router.urls,)
