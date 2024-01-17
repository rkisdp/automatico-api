from django.urls import path

from . import views

app_name = "vehicles"


urlpatterns = (
    path("<int:id>/", views.VehicleView.as_view(), name="detail"),
    path("<int:id>/photo/", views.VehiclePhotoView.as_view(), name="photo"),
    path(
        "brands/",
        views.VehicleBrandViewSet.as_view({"get": "list"}),
        name="brand-list",
    ),
    path(
        "brands/<int:id>/",
        views.VehicleBrandViewSet.as_view({"get": "retrieve"}),
        name="brand-detail",
    ),
)
