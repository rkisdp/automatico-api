from django.urls import path

from . import views

app_name = "user"

urlpatterns = (
    path("", views.ProfileView().as_view(), name="profile"),
    path("image/", views.ProfileImageView().as_view(), name="image"),
    path("password/", views.ChangePasswordView().as_view(), name="password"),
)
