from django.urls import path

from . import views

app_name = "vehicles"


urlpatterns = (
    path("/<int:vehicle_id>", views.VehicleView.as_view(), name="detail"),
    path(
        "/<int:vehicle_id>/photo",
        views.VehiclePhotoView.as_view(),
        name="photo",
    ),
    path(
        "/brands",
        views.VehicleBrandViewSet.as_view({"get": "list"}),
        name="brand-list",
    ),
    path(
        "/brands/<int:brand_id>",
        views.VehicleBrandViewSet.as_view({"get": "retrieve"}),
        name="brand-detail",
    ),
)
