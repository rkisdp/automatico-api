from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("", views.ProfileView().as_view(), name="profile"),
    path("password/", views.PasswordView().as_view(), name="password"),
]
