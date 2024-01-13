from django.urls import path

from . import views

app_name = "user"

urlpatterns = (
    path("", views.UserProfileView().as_view(), name="profile"),
    path("photo/", views.UserPhotoView().as_view(), name="photo"),
    path("password/", views.ChangePasswordView().as_view(), name="password"),
    path("vehicles/", views.UserVehicleView().as_view(), name="vehicles"),
)
