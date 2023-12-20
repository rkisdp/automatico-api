from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = "security"

urlpatterns = [
    path(
        "token/", jwt_views.TokenObtainPairView().as_view(), name="token-pair"
    ),
    path(
        "token/verify/",
        jwt_views.TokenVerifyView().as_view(),
        name="token-verify",
    ),
    path(
        "password/reset/",
        views.PasswordResetView().as_view(),
        name="password-reset",
    ),
]
