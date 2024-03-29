from __future__ import annotations

from os import path
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel


def rename(instance: VehicleBrand, filename: str) -> str:
    ext = filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    return path.join("vehicles", "brands", "images", filename)


class VehicleBrand(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Vehicle brand id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("vehicle brand"),
        help_text=_("Vehicle brand"),
        max_length=50,
        unique=True,
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Image"),
        upload_to=rename,
        null=True,
        blank=True,
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
        verbose_name = _("vehicle brand")
        verbose_name_plural = _("vehicle brands")
        db_table = "vehicle_brand"

    def __str__(self) -> str:
        return self.name
