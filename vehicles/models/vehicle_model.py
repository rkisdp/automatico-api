from __future__ import annotations

from os import path
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .vehicle_brand_model import VehicleBrandModel


def rename(instance: VehicleModel, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("vehicles", "photos", filename)


class VehicleModel(models.Model):
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
        to=VehicleBrandModel,
        on_delete=models.PROTECT,
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
    )
    nickname = models.CharField(
        verbose_name=_("nickname"),
        help_text=_("Nickname"),
        max_length=50,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        verbose_name=_("owner"),
        help_text=_("Owner"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="vehicles",
        null=True,
        blank=True,
    )
    vin = models.CharField(
        verbose_name=_("vin"),
        help_text=_("VIN"),
        max_length=17,
    )
    photo = models.ImageField(
        verbose_name=_("photo"),
        help_text=_("Photo"),
        upload_to=rename,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")
        db_table = "vehicle"

    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year}"
