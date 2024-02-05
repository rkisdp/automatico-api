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
        r"^/image/?$",
        views.UserPhotoView().as_view(),
        name="image",
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
        r"^/workshops/favorites/?$",
        views.UserFavoriteWorkshopListView().as_view(),
        name="favorite-workshops",
    ),
    re_path(
        r"^/workshops/favorites/(?P<workshop_id>\d+)/?$",
        views.UserFavoriteWorkshopView().as_view(),
        name="favorite-workshops",
    ),
    re_path(
        r"^/workshops/services/?$",
        views.UserWorkshopServiceView().as_view(),
        name="workshops-services",
    ),
)
