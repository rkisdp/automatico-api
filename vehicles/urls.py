from django.urls import path

from . import views

app_name = "vehicles"


urlpatterns = (
    path(
        "/<int:vehicle_id>",
        views.VehicleView.as_view(),
        name="detail",
    ),
    path(
        "/<int:vehicle_id>/image",
        views.VehiclePhotoView.as_view(),
        name="image",
    ),
    path(
        "/brands",
        views.VehicleBrandListView.as_view(),
        name="brand-list",
    ),
)
