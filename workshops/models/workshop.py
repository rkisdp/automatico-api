from __future__ import annotations

from datetime import timedelta
from os import path
from uuid import uuid4

from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from vehicles.models import Vehicle, VehicleBrand

from .speciality import Speciality


def rename(instance: Workshop, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("workshops", "images", filename)


class Workshop(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("The workshop ID."),
        primary_key=True,
        unique=True,
        editable=False,
    )
    owner = models.ForeignKey(
        verbose_name=_("owner"),
        help_text=_("The account owner of the workshop."),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="workshops",
    )
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_(
            "The name of the workshop. This field is not case sensitive."
        ),
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("The workshop description."),
        max_length=500,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("The workshop image."),
        upload_to=rename,
        null=True,
        blank=True,
    )
    banner = models.ImageField(
        verbose_name=_("banner"),
        help_text=_("The workshop banner."),
        upload_to=rename,
        null=True,
        blank=True,
    )
    location = models.PointField(
        verbose_name=_("location"),
        help_text=_("The workshop location."),
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        verbose_name=_("employees"),
        help_text=_("The workshop employees"),
        to=settings.AUTH_USER_MODEL,
        related_name="workplace",
        blank=True,
    )
    brands = models.ManyToManyField(
        verbose_name=_("brands"),
        help_text=_("The brands of vehicles the workshop works with"),
        to=VehicleBrand,
        related_name="workshop_brands",
        blank=True,
    )
    specialities = models.ManyToManyField(
        verbose_name=_("specialities"),
        help_text=_("Workshop specialities"),
        to=Speciality,
        related_name="workshop_specialities",
        blank=True,
    )
    vehicles = models.ManyToManyField(
        verbose_name=_("vehicles"),
        help_text=_("Workshop vehicles"),
        to=Vehicle,
        related_name="workshop_vehicles",
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        help_text=_("Whether the workshop is active or not."),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("The date and time the workshop was created."),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("The date and time the workshop was last updated."),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("workshop")
        verbose_name_plural = _("workshops")
        db_table = "workshop"

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def validate_unique_name(name: str) -> None:
        if Workshop.objects.filter(name__iexact=name).exists():
            raise ValidationError(
                {"name": _("Workshop with this name already exists.")}
            )

    @property
    def rating(self) -> float:
        return (
            self.reviews.aggregate(rating=models.Avg("rating"))["rating"] or 4
        )

    @property
    def recent_rating(self) -> float:
        if hasattr(self, "_recent_rating"):
            return self._recent_rating
        return (
            self.reviews.filter(
                created_at__gte=timezone.now() - timedelta(days=30),
            ).aggregate(rating=models.Avg("rating"))["rating"]
            or 4
        )

    @recent_rating.setter
    def recent_rating(self, value: float) -> None:
        self._recent_rating = value
