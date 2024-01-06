from django.urls import path

from . import views

app_name = "security"

urlpatterns = (
    path(
        "account/activation/",
        views.AccountActivationView().as_view(),
        name="account-activation",
    ),
    path(
        "account/activation/resend/",
        views.ResendAccountActivationCodeView().as_view(),
        name="resend-account-activation-code",
    ),
    path(
        "email/verification/",
        views.EmailVerificationView().as_view(),
        name="email-verification",
    ),
    path(
        "email/verification/resend/",
        views.ResendEmailVerificationCodeView().as_view(),
        name="resend-email-verification-code",
    ),
    path(
        "password/reset/",
        views.PasswordResetView().as_view(),
        name="password-reset",
    ),
    path(
        "password/reset/confirm/",
        views.ConfirmPasswordResetView().as_view(),
        name="password-reset-confirm",
    ),
    path("sign-up/", views.SignUpView().as_view(), name="sign-up"),
    path("token/", views.AccessTokenView().as_view(), name="access-token"),
)
