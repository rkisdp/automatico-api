from __future__ import annotations

from os import path
from uuid import uuid4

from django.conf import settings
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel

from .vehicle_brand import VehicleBrand


def rename(instance: Vehicle, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("vehicles", "images", filename)


class Vehicle(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Service id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    brand = models.ForeignKey(
        verbose_name=_("brand"),
        help_text=_("Brand"),
        to=VehicleBrand,
        on_delete=models.DO_NOTHING,
        related_name="vehicles",
    )
    model = models.CharField(
        verbose_name=_("model"),
        help_text=_("Model"),
        max_length=50,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name=_("year"),
        help_text=_("Year"),
        null=True,
        blank=True,
        validators=(
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ),
    )
    nickname = models.CharField(
        verbose_name=_("nickname"),
        help_text=_("Nickname"),
        max_length=50,
    )
    owner = models.ForeignKey(
        verbose_name=_("owner"),
        help_text=_("Owner"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="vehicles",
        null=True,
        blank=True,
    )
    plate = models.CharField(
        verbose_name=_("plate"),
        help_text=_("Plate"),
        max_length=8,
        null=True,
        blank=True,
        validators=(
            RegexValidator(
                regex=(
                    r"^((A{1,2}|B|C|D{1,2}|F|G|L|H|I|T|P{1,2}|U|J|R|S|M|O[EFMPI"
                    r"]|E[AGLMEIDX]|VC|WD|YX|N?Z)\d{6})|(K\d{7})$"
                ),
                message=_("Plate must be in the format 'A000000'."),
            ),
        ),
    )
    vin = models.CharField(
        verbose_name=_("vin"),
        help_text=_("VIN"),
        max_length=17,
        null=True,
        blank=True,
        validators=(
            RegexValidator(
                regex=r"^[A-HJ-NPR-Z\d]{8}[\dX][A-HJ-NPR-Z\d]{2}\d{6}$",
                message=_("Invalid VIN format."),
            ),
        ),
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Image"),
        upload_to=rename,
        null=True,
        blank=True,
    )
    is_archived = models.BooleanField(
        verbose_name=_("archived"),
        help_text=_("Archived"),
        default=False,
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
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")
        unique_together = (
            ("nickname", "owner", "deleted_at"),
            ("vin", "owner", "deleted_at"),
            ("plate", "owner", "deleted_at"),
        )
        db_table = "vehicle"

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def save(self, *args, **kwargs) -> None:
        if self.plate is not None:
            self.plate = self.plate.upper()

        if self.vin is not None:
            self.vin = self.vin.upper()
        super().save(*args, **kwargs)
