from __future__ import annotations

from os import path
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from vehicles.models import VehicleBrandModel, VehicleModel

from .speciality_model import SpecialityModel


def rename(instance: WorkshopModel, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("workshops", "photos", filename)


class WorkshopModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Workshop id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    owner = models.ForeignKey(
        verbose_name=_("owner"),
        help_text=_("Owner"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="workshops",
    )
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Workshop name"),
        max_length=100,
        unique=True,
    )
    photo = models.ImageField(
        verbose_name=_("photo"),
        help_text=_("Workshop photo"),
        upload_to=rename,
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        verbose_name=_("latitude"),
        help_text=_("Workshop latitude"),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name=_("longitude"),
        help_text=_("Workshop longitude"),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        verbose_name=_("employees"),
        help_text=_("Workshop employees"),
        to=settings.AUTH_USER_MODEL,
        related_name="workshop_empoyees",
        blank=True,
    )
    brands = models.ManyToManyField(
        verbose_name=_("brands"),
        help_text=_("Workshop brands"),
        to=VehicleBrandModel,
        related_name="workshop_brands",
        blank=True,
    )
    specialities = models.ManyToManyField(
        verbose_name=_("specialities"),
        help_text=_("Workshop specialities"),
        to=SpecialityModel,
        related_name="workshop_specialities",
        blank=True,
    )
    vehicles = models.ManyToManyField(
        verbose_name=_("vehicles"),
        help_text=_("Workshop vehicles"),
        to=VehicleModel,
        related_name="workshop_vehicles",
        blank=True,
    )

    class Meta:
        verbose_name = _("workshop")
        verbose_name_plural = _("workshops")
        db_table = "workshop"

    def __str__(self) -> str:
        return self.name
