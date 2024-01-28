from django.urls import re_path

from . import views

app_name = "security"

urlpatterns = (
    re_path(
        r"^/account/activation/?$",
        views.AccountActivationView().as_view(),
        name="account-activation",
    ),
    re_path(
        r"^/account/activation/resend/?$",
        views.ResendAccountActivationCodeView().as_view(),
        name="resend-account-activation-code",
    ),
    re_path(
        r"^/account/activation/validate/?$",
        views.ValidateAccountActivationCodeView().as_view(),
        name="validate-account-activation-code",
    ),
    re_path(
        r"^/email/verification/?$",
        views.EmailVerificationView().as_view(),
        name="email-verification",
    ),
    re_path(
        r"^/email/verification/resend/?$",
        views.ResendEmailVerificationCodeView().as_view(),
        name="resend-email-verification-code",
    ),
    re_path(
        r"^/password/reset/?$",
        views.PasswordResetView().as_view(),
        name="password-reset",
    ),
    re_path(
        r"^/password/reset/confirm/?$",
        views.ConfirmPasswordResetView().as_view(),
        name="password-reset-confirm",
    ),
    re_path(
        r"^/password/reset/validate/?$",
        views.ValidatePasswordResetCodeView().as_view(),
        name="validate-account-activation-code",
    ),
    re_path(
        r"^/sign-up/?$",
        views.SignUpView().as_view(),
        name="sign-up",
    ),
    re_path(
        r"^/token/?$",
        views.AccessTokenView().as_view(),
        name="access-token",
    ),
)
