from __future__ import annotations

from os import path
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel
from rest_framework.exceptions import ValidationError


def rename(instance: Speciality, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("workshops", "reviews", "images", filename)


class Speciality(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Speciality id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("speciality"),
        help_text=_("Workshop speciality"),
        max_length=50,
        unique=True,
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Image"),
        upload_to=rename,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("The date and time of creation."),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("The date and time of last update."),
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("speciality")
        verbose_name_plural = _("specialities")
        db_table = "speciality"

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def validate_unique_name(name: str) -> None:
        if Speciality.objects.filter(name__iexact=name).exists():
            raise ValidationError(
                {"name": _("Speciality with this name already exists.")}
            )
