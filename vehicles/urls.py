from django.urls import re_path

from . import views

app_name = "vehicles"


urlpatterns = (
    re_path(
        r"^/(?P<vehicle_id>\d+)/$",
        views.VehicleView.as_view(),
        name="detail",
    ),
    re_path(
        r"^/(?P<vehicle_id>\d+)/image/?$",
        views.VehiclePhotoView.as_view(),
        name="image",
    ),
    re_path(
        r"^/brands/?$",
        views.VehicleBrandListView.as_view(),
        name="brand-list",
    ),
)
