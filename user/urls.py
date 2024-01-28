from django.urls import re_path

from . import views

app_name = "user"

urlpatterns = (
    re_path(
        r"^/?$",
        views.UserProfileView().as_view(),
        name="profile",
    ),
    re_path(
        r"^/password/?$",
        views.ChangePasswordView().as_view(),
        name="password",
    ),
    re_path(
        r"^/photo/?$",
        views.UserPhotoView().as_view(),
        name="photo",
    ),
    re_path(
        r"^/services/?$",
        views.UserServiceView().as_view(),
        name="services",
    ),
    re_path(
        r"^/vehicles/?$",
        views.UserVehicleView().as_view(),
        name="vehicles",
    ),
    re_path(
        r"^/workshops/?$",
        views.UserWorkshopView().as_view(),
        name="workshops",
    ),
    re_path(
        r"^/workshops/services/?$",
        views.UserWorkshopServiceView().as_view(),
        name="workshops-services",
    ),
)
