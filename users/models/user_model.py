from __future__ import annotations

from os import path
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..managers import UserManager


def rename(instance: UserModel, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("users", "photos", filename)


class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("User id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    first_name = models.CharField(
        verbose_name=_("first name"),
        help_text=_("User legal first name"),
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name=_("last name"),
        help_text=_("User legal last name"),
        max_length=50,
    )
    email = models.EmailField(
        verbose_name=_("email"),
        help_text=_("User email"),
        unique=True,
        max_length=255,
        error_messages={
            "unique": _("A user with that email already exists"),
        },
    )
    email_verified = models.BooleanField(
        verbose_name=_("email verified"),
        help_text=_("User email verification status"),
        default=False,
    )
    password = models.CharField(
        verbose_name=_("password"),
        help_text=_("User hashed password"),
        max_length=128,
    )
    photo = models.ImageField(
        verbose_name=_("photo"),
        help_text=_("User profile photo"),
        upload_to=rename,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        help_text=_("User phone number"),
        max_length=15,
        blank=True,
        null=True,
    )
    phone_number_verified = models.BooleanField(
        verbose_name=_("phone number verified"),
        help_text=_("User phone number verified"),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"),
        help_text=_("User registration date"),
        default=timezone.now,
        editable=False,
    )
    last_login = models.DateTimeField(
        verbose_name=_("last login"),
        help_text=_("User last login date"),
        blank=True,
        null=True,
        editable=False,
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "user"

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
