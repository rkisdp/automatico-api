from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags

from security.models import VerificationCode, VerificationCodeType


def _gen_verification_code() -> str:
    return get_random_string(length=4, allowed_chars="1234567890")


def send_verification_code(
    user,
    code_type: str,
    email_template: str,
    email_subject: str,
) -> None:
    if hasattr(user, "verification_code"):
        user.verification_code.delete()

    code = _gen_verification_code()

    verification_code_type = VerificationCodeType.objects.get(
        code__iexact=code_type
    )
    VerificationCode.objects.create(
        user=user, type=verification_code_type, code=make_password(code)
    )

    html_message = render_to_string(
        f"emails/{email_template}.html",
        {
            "user": user,
            "verification_code": code,
        },
    )
    del code

    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject=f"{email_subject} - AutoMático",
        body=plain_message,
        to=[user.email],
    )

    message.attach_alternative(html_message, "text/html")
    message.send()
