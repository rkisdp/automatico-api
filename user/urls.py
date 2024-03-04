from django.urls import path

from . import views

app_name = "user"

urlpatterns = (
    path(
        "",
        views.UserProfileView().as_view(),
        name="profile",
    ),
    path(
        "/password",
        views.ChangePasswordView().as_view(),
        name="password",
    ),
    path(
        "/image",
        views.UserPhotoView().as_view(),
        name="image",
    ),
    path(
        "/services",
        views.UserServiceView().as_view(),
        name="services",
    ),
    path(
        "/vehicles",
        views.UserVehicleView().as_view(),
        name="vehicles",
    ),
    path(
        "/workshops",
        views.UserWorkshopView().as_view(),
        name="workshops",
    ),
    path(
        "/workshops/favorites",
        views.UserFavoriteWorkshopListView().as_view(),
        name="favorite-workshops",
    ),
    path(
        "/workshops/favorites/<int:workshop_id>",
        views.UserFavoriteWorkshopView().as_view(),
        name="favorite-workshops",
    ),
    path(
        "/workshops/services",
        views.UserWorkshopServiceView().as_view(),
        name="workshops-services",
    ),
)
